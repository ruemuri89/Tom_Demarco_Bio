document.addEventListener("DOMContentLoaded", () => {
    gsap.registerPlugin(ScrollTrigger);

    // Fade-in blocks
    gsap.utils.toArray("[data-gsap='fade-in']").forEach(el => {
        gsap.from(el, {
            opacity: 0,
            y: 40,
            duration: 1.2,
            ease: "power3.out",
            scrollTrigger: {
                trigger: el,
                start: "top 85%",
            }
        });
    });

    // Fade-up blocks
    gsap.utils.toArray("[data-gsap='fade-up']").forEach(el => {
        gsap.from(el, {
            opacity: 0,
            y: 60,
            duration: 1.3,
            ease: "power3.out",
            scrollTrigger: {
                trigger: el,
                start: "top 80%",
            }
        });
    });

    // Fade-left / fade-right
    gsap.utils.toArray("[data-gsap='fade-left']").forEach(el => {
        gsap.from(el, {
            opacity: 0,
            x: -70,
            duration: 1.4,
            ease: "power3.out",
            scrollTrigger: {
                trigger: el,
                start: "top 80%",
            }
        });
    });

    gsap.utils.toArray("[data-gsap='fade-right']").forEach(el => {
        gsap.from(el, {
            opacity: 0,
            x: 70,
            duration: 1.4,
            ease: "power3.out",
            scrollTrigger: {
                trigger: el,
                start: "top 80%",
            }
        });
    });

    // Pop animation for concept cards
    gsap.utils.toArray("[data-gsap='pop']").forEach(el => {
        gsap.from(el, {
            scale: 0.8,
            opacity: 0,
            duration: 0.9,
            delay: Math.random() * 0.4,
            ease: "back.out(1.7)",
            scrollTrigger: {
                trigger: el,
                start: "top 85%",
            }
        });
    });

    // Floating influence tags
    gsap.utils.toArray("[data-gsap='float']").forEach(el => {
        gsap.to(el, {
            y: () => (Math.random() * 40 - 20),
            x: () => (Math.random() * 40 - 20),
            duration: 3 + Math.random() * 3,
            repeat: -1,
            yoyo: true,
            ease: "sine.inOut"
        });
    });
});
