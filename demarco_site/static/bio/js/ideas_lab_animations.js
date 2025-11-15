document.addEventListener("DOMContentLoaded", () => {

    /* ---------------------------------------------------------
       ORGANIC, RANDOMIZED ANIMATION HELPERS
       --------------------------------------------------------- */

    // Returns a random float within a range
    const rand = (min, max) => Math.random() * (max - min) + min;

    // Returns a random easing from a small approved library
    const randomEase = () => {
        const eases = ["power2.out", "power3.out", "power1.inOut", "back.out(1.7)"];
        return eases[Math.floor(Math.random() * eases.length)];
    };

    /* ---------------------------------------------------------
       ANIMATE WIDGETS WITH RANDOMIZED TIMING + EASING
       --------------------------------------------------------- */

    gsap.from(".widget", {
        opacity: 0,
        y: () => rand(15, 40),        // Random vertical offset
        duration: () => rand(0.6, 1), // Random duration
        stagger: {
            each: rand(0.05, 0.2),    // Slight stagger difference
            from: "random"            // Organic random staggering
        },
        ease: () => randomEase()
    });

    /* ---------------------------------------------------------
       ANIMATE CONCEPT HEADERS WITH RANDOMIZED PROPERTIES
       --------------------------------------------------------- */

    gsap.from("h1, h2", {
        opacity: 0,
        y: () => rand(10, 30),
        duration: () => rand(0.4, 0.9),
        ease: () => randomEase(),
        stagger: () => rand(0.05, 0.25)
    });

    /* ---------------------------------------------------------
       MICRO-INTERACTIONS FOR INPUTS
       --------------------------------------------------------- */

    document.querySelectorAll("input[type=range]").forEach(range => {
        range.addEventListener("input", () => {
            gsap.to(range, {
                scale: () => rand(1.03, 1.08),
                duration: 0.12,
                yoyo: true,
                repeat: 1,
                ease: "power1.out"
            });
        });
    });

    /* ---------------------------------------------------------
       MONTE CARLO BUTTON POP EFFECT
       --------------------------------------------------------- */

    document.querySelectorAll("#runMonteCarlo").forEach(btn => {
        btn.addEventListener("click", () => {
            gsap.fromTo(btn,
                {
                    scale: 1
                },
                {
                    scale: () => rand(1.07, 1.12),
                    duration: 0.12,
                    yoyo: true,
                    repeat: 1,
                    ease: "back.out(2)"
                }
            );
        });
    });

});
