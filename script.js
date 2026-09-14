// 1. الأنيميشن بتاع كتابة الكلام
const words = ["Computer Science Student @ Ain Shams", "Web & Python Developer"];
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

// 2. زرار الوضع الليلي (Dark Mode)
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// عشان نربط الزرار بالحدث (Click)
themeToggle.addEventListener('click', () => {
    // التبديل بين الكلاس الأساسي والوضع الليلي
    body.classList.toggle('dark-mode');
    
    // تغيير الأيقونة بين القمر والشمس
    if (body.classList.contains('dark-mode')) {
        themeToggle.className = 'fas fa-sun'; // شمس في الوضع الليلي
    } else {
        themeToggle.className = 'fas fa-moon'; // قمر في الوضع الفاتح
    }
});

// 3. الأنيميشن الانسيابي عند النزول (Scroll Animations)
const hiddenElements = document.querySelectorAll('.hidden');

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        }
    });
}, { threshold: 0.1 }); // الأنيميشن يشتغل لما 10% من القسم يظهر

hiddenElements.forEach((el) => observer.observe(el));

// تشغيل وظيفة الكتابة بعد تحميل الصفحة
document.addEventListener("DOMContentLoaded", () => {
    setTimeout(type, 1000);
});