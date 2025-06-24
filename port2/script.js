const questions = document.querySelectorAll(".question");

questions.forEach((q) => {
    q.addEventListener("click", (e) => {
        const id = "a" + q.id.substring(1,2);
        const answer = document.getElementById(id);
        q.classList.toggle("active");
        answer.classList.toggle("active");
    });
});