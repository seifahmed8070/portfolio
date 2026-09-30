const words = ["Computer Science Student", "Python Developer", "Tech Enthusiast"];
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;
const typingElement = document.querySelector('.typing-text');

function type() {
    if (!typingElement) return;
    const currentWord = words[wordIndex];
    
    if (isDeleting) {
        typingElement.textContent = currentWord.substring(0, charIndex - 1);
        charIndex--;
    } else {
        typingElement.textContent = currentWord.substring(0, charIndex + 1);
        charIndex++;
    }

    let typeSpeed = isDeleting ? 50 : 100;

    if (!isDeleting && charIndex === currentWord.length) {
        typeSpeed = 2000;
        isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        typeSpeed = 500;
    }

    setTimeout(type, typeSpeed);
}

const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
const body = document.body;

toggleSwitch.addEventListener('change', function(e) {
    if (e.target.checked) {
        body.classList.add('dark-mode');
    } else {
        body.classList.remove('dark-mode');
    }
});

const hiddenElements = document.querySelectorAll('.hidden');
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        }
    });
}, { threshold: 0.15 });

hiddenElements.forEach((el) => observer.observe(el));

function openModal() {
    const modal = document.getElementById("certModal");
    modal.style.display = "block";
}

function closeModal() {
    const modal = document.getElementById("certModal");
    modal.style.display = "none";
}

document.addEventListener("DOMContentLoaded", () => {
    setTimeout(type, 1000);
});