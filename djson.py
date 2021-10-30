
class Quiz:
    def __init__(self):
        self.q_no = 0
        self.data_size = 5
        self.correct = 0

    def display_result(self):
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        return ("Result", f"{result}\n{correct}\n{wrong}")

        # This method checks the Answer after we click on Next.

    def check_ans(self, q_no, g):
        if g == int(data["answer"[q_no]]):
            # if the option is correct it return true
            print("you answer is correct")
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1

            self.q_no += 1

        # checks if the q_no size is equal to the data size
        if self.q_no == self.data_size:
            print("end")


quiz = Quiz()
