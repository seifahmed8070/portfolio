/* =========================================
   المتغيرات الأساسية (لازم تكون فوق)
========================================= */
const langBtn = document.getElementById('lang-btn');
const typingElement = document.querySelector('.typing-text');

let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;
let currentLang = localStorage.getItem('siteLang') || 'en';
window.cvAlertMsg = "My CV will be available soon!";

const typingWords = {
    en: ["Computer Science Student", "Python Developer", "Tech Enthusiast"],
    ar: ["طالب علوم حاسب", "مطور بايثون", "شغوف بالتقنية"]
};
let words = typingWords[currentLang];


/* =========================================
   نظام الترجمة (English / Arabic Toggle)
========================================= */
const translations = {
    en: {
        "title": "Seif Ahmed | Portfolio",
        "nav-about": "About",
        "nav-education": "Education",
        "nav-skills": "Skills",
        "nav-projects": "Projects",
        "nav-certificates": "Certificates",
        "nav-contact": "Contact",
        "hero-avail": "<span class='pulse-dot'></span> Available for Opportunities",
        "hero-hi": "Hi, I'm <span class='gradient-text'>Seif Ahmed</span>",
        "hero-iam": "I am a ",
        "hero-desc": "Passionate CS student creating modern web applications and smart Python solutions.",
        "hero-btn-work": "View My Work <i class='fas fa-arrow-right'></i>",
        "hero-btn-cv": "Download CV <i class='fas fa-download'></i>",
        "edu-title": "My <span class='gradient-text'>Education</span>",
        "edu-fac": "Faculty of Computers and Information Science \"FCIS\"",
        "edu-uni": "Ain Shams University \"ASU\"",
        "edu-desc": "Starting my academic journey in 2026 with a strong mathematical background. Passionate about software development, algorithms, and mastering new technologies.",
        "skills-title": "My <span class='gradient-text'>Skills & Roadmap</span>",
        "skills-sub": "What I use now, and what I am eager to master next.",
        "skills-core": "Core Stack",
        "skills-next": "Learning Next (Roadmap)",
        "skill-db": "Databases & SQL",
        "skill-ds": "Data Structures",
        "badge-soon-1": "Soon",
        "badge-soon-2": "Soon",
        "badge-soon-3": "Soon",
        "proj-title": "My <span class='gradient-text'>Projects</span>",
        "p1-title": "Python Adventure Game",
        "p1-desc": "A text-based interactive choice game built with Python logic and structured code.",
        "p1-link": "Play Game <i class='fas fa-play'></i>",
        "p2-title": "Portfolio Website",
        "p2-desc": "My personal responsive portfolio built using modern web technologies.",
        "p2-link": "Live Demo <i class='fas fa-arrow-right'></i>",
        "p3-title": "Multi-Page Blog",
        "p3-desc": "A responsive multi-page blog layout featuring tech, health, and travel posts using semantic HTML and CSS.",
        "p3-link": "Live Demo <i class='fas fa-arrow-right'></i>",
        "cert-title": "Certificates & <span class='gradient-text'>Achievements</span>",
        "c1-title": "Programming Basics",
        "c1-desc": "Verified certificate of completion in programming fundamentals.",
        "c1-link": "View Full Size <i class='fas fa-expand'></i>",
        "contact-title": "Get In <span class='gradient-text'>Touch</span>",
        "contact-desc": "Feel free to reach out for collaborations or inquiries!",
        "contact-link": "Send Email <i class='fas fa-paper-plane'></i>"
    },
    ar: {
        "title": "سيف أحمد | بورتفوليو",
        "nav-about": "من أنا",
        "nav-education": "التعليم",
        "nav-skills": "المهارات",
        "nav-projects": "المشاريع",
        "nav-certificates": "الشهادات",
        "nav-contact": "تواصل معي",
        "hero-avail": "<span class='pulse-dot'></span> متاح لفرص العمل",
        "hero-hi": "أهلاً، أنا <span class='gradient-text'>سيف أحمد</span>",
        "hero-iam": "أنا ",
        "hero-desc": "طالب شغوف بعلوم الحاسب، أطور تطبيقات ويب حديثة وحلول برمجية ذكية باستخدام بايثون.",
        "hero-btn-work": "شاهد أعمالي <i class='fas fa-arrow-left'></i>",
        "hero-btn-cv": "تحميل السيرة الذاتية <i class='fas fa-download'></i>",
        "edu-title": "<span class='gradient-text'>تعليمي</span> الأكاديمي",
        "edu-fac": "كلية الحاسبات والمعلومات",
        "edu-uni": "جامعة عين شمس",
        "edu-desc": "بدأت رحلتي الأكاديمية بخلفية قوية في الرياضيات. شغوف بتطوير البرمجيات والخوارزميات وتعلم التقنيات الجديدة.",
        "skills-title": "<span class='gradient-text'>مهاراتي وخطتي</span>",
        "skills-sub": "التقنيات التي أستخدمها حالياً، وما أتطلع لتعلمه لاحقاً.",
        "skills-core": "المهارات الأساسية",
        "skills-next": "خريطة الطريق (قيد التعلم)",
        "skill-db": "قواعد البيانات و SQL",
        "skill-ds": "هياكل البيانات",
        "badge-soon-1": "قريباً",
        "badge-soon-2": "قريباً",
        "badge-soon-3": "قريباً",
        "proj-title": "<span class='gradient-text'>مشاريعي</span>",
        "p1-title": "لعبة مغامرات بايثون",
        "p1-desc": "لعبة تفاعلية تعتمد على النصوص والاختيارات، مبنية باستخدام منطق بايثون وكود منظم.",
        "p1-link": "العب الآن <i class='fas fa-play'></i>",
        "p2-title": "موقع البورتفوليو",
        "p2-desc": "موقع البورتفوليو الشخصي الخاص بي، متجاوب مع جميع الشاشات ومبني بأحدث تقنيات الويب.",
        "p2-link": "عرض حي <i class='fas fa-arrow-left'></i>",
        "p3-title": "مدونة متعددة الصفحات",
        "p3-desc": "مدونة متجاوبة تحتوي على مقالات في التقنية، الصحة، والسفر باستخدام HTML و CSS.",
        "p3-link": "عرض حي <i class='fas fa-arrow-left'></i>",
        "cert-title": "الشهادات و <span class='gradient-text'>الإنجازات</span>",
        "c1-title": "أساسيات البرمجة",
        "c1-desc": "شهادة إتمام معتمدة في أساسيات ومبادئ البرمجة.",
        "c1-link": "عرض الحجم الكامل <i class='fas fa-expand'></i>",
        "contact-title": "تواصل <span class='gradient-text'>معي</span>",
        "contact-desc": "لا تتردد في التواصل معي للتعاون أو لأي استفسارات!",
        "contact-link": "إرسال رسالة <i class='fas fa-paper-plane'></i>"
    }
};

function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('siteLang', lang);

    // تغيير اتجاه الصفحة واسم الزرار
    document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
    document.documentElement.lang = lang;
    if (langBtn) langBtn.textContent = lang === 'ar' ? 'English' : 'عربي';

    // ترجمة العنوان فوق في التاب
    document.title = translations[lang]["title"];
    window.cvAlertMsg = lang === 'ar' ? "سيرتي الذاتية ستكون متاحة قريباً!" : "My CV will be available soon!";

    // ترجمة كل النصوص 
    const elements = document.querySelectorAll('[data-key]');
    elements.forEach(el => {
        const key = el.getAttribute('data-key');
        if (translations[lang][key]) {
            el.innerHTML = translations[lang][key];
        }
    });

    // إعادة ضبط تأثير الكتابة عشان يترجم
    words = typingWords[lang];
    wordIndex = 0;
    charIndex = 0;
    isDeleting = false;
    if (typingElement) typingElement.textContent = "";
}

// تشغيل التبديل عند الضغط
if (langBtn) {
    langBtn.addEventListener('click', () => {
        setLanguage(currentLang === 'en' ? 'ar' : 'en');
    });
}

// تهيئة اللغة عند التحميل
setLanguage(currentLang);


/* =========================================
   باقي الأكواد (الكتابة، الدارك مود، الأنيميشن)
========================================= */

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

if (toggleSwitch) {
    toggleSwitch.addEventListener('change', function(e) {
        if (e.target.checked) {
            body.classList.add('dark-mode');
        } else {
            body.classList.remove('dark-mode');
        }
    });
}

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
    if (modal) modal.style.display = "block";
}

function closeModal() {
    const modal = document.getElementById("certModal");
    if (modal) modal.style.display = "none";
}

document.addEventListener("DOMContentLoaded", () => {
    setTimeout(type, 1000);
});