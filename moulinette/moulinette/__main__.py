# ABOUTME: CLI entry point for the moulinette evaluation tool.
# ABOUTME: Provides commands to evaluate student RAG search results and list valid questions.

from moulinette.models import (
    StudentSearchResultsAndAnswer,
    StudentSearchResults,
    RagDataset,
)
import json
from pathlib import Path
import fire
from moulinette.validate_student_data import validate_student_data
from moulinette.evaluate_retrieval import (
    calculate_recall_at_k_on_dataset,
    build_eval_objects,
    calculate_recall_at_k_for_one_question,
)

def load_json(path: str):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_student_search_results(student_search_results_path: str):
    return StudentSearchResults(**load_json(student_search_results_path))


def load_student_answers(student_answers_path: str):
    return StudentSearchResultsAndAnswer(**load_json(student_answers_path))


def load_dataset_questions_and_answers(dataset_path: str):
    return RagDataset(**load_json(dataset_path))


class Moulinette:
    def evaluate_student_search_results(
        self, 
        student_answer_path: str, 
        dataset_path: str,
		k: int = 10,
		max_context_length: int = 2000,
    ):
        student_search_results = load_student_search_results(student_answer_path)

        is_valid = validate_student_data(
            student_search_results, 
            max_context_length=max_context_length, 
            k=k
        )
        if not is_valid:
            print("Student search results are not valid")
            return False

        recall_results = calculate_recall_at_k_on_dataset(
            student_search_results, 
            load_dataset_questions_and_answers(dataset_path),
            minimal_iou_threshold=0.01,
            k_values=[1, 3, 5, 10],
        )
        print(recall_results)
        if recall_results["recall@5"] < 0.45:
            print("Student search results are not valid")
            return False
        return True

    def list_valid_questions(
        self,
        student_answer_path: str,
        dataset_path: str,
        k: int = 10,
        require_all_sources: bool = True,
        minimal_iou_threshold: float = 0.01,
    ):
        """List which dataset questions have their sources successfully retrieved.

        Args:
            student_answer_path: Path to student search results JSON.
            dataset_path: Path to RAG dataset JSON with ground-truth sources.
            k: Number of top results to consider per question.
            require_all_sources: If True, a question is valid only when recall@k == 1.0.
                If False, any recall > 0 counts as valid.
            minimal_iou_threshold: Minimum IoU overlap to count a source as found.
        """
        student_search_results = load_student_search_results(student_answer_path)
        rag_dataset = load_dataset_questions_and_answers(dataset_path)
        eval_objects = build_eval_objects(student_search_results, rag_dataset)

        # Build question_id -> question text lookup from dataset
        question_texts = {}
        for q in rag_dataset.rag_questions:
            question_texts[q.question_id] = q.question

        # ANSI color codes
        GREEN = "\033[32m"
        RED = "\033[31m"
        RESET = "\033[0m"
        BOLD = "\033[1m"

        mode_label = "all_sources" if require_all_sources else "any_source"
        valid_count = 0
        total_count = len(eval_objects)
        lines = []

        for qid, eval_obj in eval_objects.items():
            recall = calculate_recall_at_k_for_one_question(
                eval_obj.pred_sources[:k],
                eval_obj.true_sources,
                minimal_iou_threshold,
            )
            if require_all_sources:
                is_valid = recall == 1.0
            else:
                is_valid = recall > 0

            if is_valid:
                valid_count += 1
                tag = f"{GREEN}[VALID]{RESET}  "
            else:
                tag = f"{RED}[INVALID]{RESET}"

            q_text = question_texts.get(qid, qid)
            lines.append(f"  {tag} {qid}  \"{q_text}\"")

        print(f"\n{BOLD}=== Valid Questions ({valid_count}/{total_count}, k={k}, mode={mode_label}) ==={RESET}\n")
        for line in lines:
            print(line)
        print(f"\n{BOLD}Summary: {valid_count}/{total_count} questions valid{RESET}")

    def evaluate_student_answers(self, student_answer_path: str):
        pass

if __name__ == "__main__":
    fire.Fire(Moulinette)