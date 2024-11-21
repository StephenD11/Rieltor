let currentIndex = 0;

function moveSlide(step) {
    const images = document.querySelectorAll('.carousel-images img');
    const totalImages = images.length;

    currentIndex = (currentIndex + step + totalImages) % totalImages; // Обеспечивает цикличность (при переходе к первой картинке после последней)

    const carouselImages = document.querySelector('.carousel-images');
    carouselImages.style.transform = `translateX(-${currentIndex * 100}%)`; // Перемещает изображения
}