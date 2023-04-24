const carousel = document.querySelector('.adsSlider')
const firstImg = document.querySelector('.slide img')
const backBtn = document.querySelector('.back')
const forwardBtn = document.querySelector('.forward')
const slides = document.querySelectorAll('.slide')
console.log(slides);
let isDragStart = false, prevPageX, prevScrollLeft, positionDiff
let firstImgWidth = firstImg.clientWidth + 25
let scrollWidth = carousel.scrollWidth - carousel.clientWidth

forwardBtn.onclick = () =>
{
    if (scrollWidth - 25 <= carousel.scrollLeft) {
        carousel.style.scrollBehavior = 'auto';
        carousel.scrollLeft = 0;
    }
    else {
        carousel.style.scrollBehavior = 'smooth';
        carousel.scrollLeft += firstImgWidth
    }
}
backBtn.onclick = () =>
{
    if (carousel.scrollLeft-25 <= 0) {
        carousel.style.scrollBehavior = 'auto';
        carousel.scrollLeft = carousel.scrollWidth
    }
    else {
        carousel.style.scrollBehavior = 'smooth';
        carousel.scrollLeft -= firstImgWidth
    }

}

const autoSlide = () =>
{
    if (scrollWidth - 25 <= carousel.scrollLeft) return
    positionDiff = Math.abs(positionDiff)
    let firstImgWidth = firstImg.clientWidth + 25
    let valDifference = firstImgWidth - positionDiff
    if (carousel.scrollLeft > prevScrollLeft) {
        return carousel.scrollLeft += positionDiff > firstImgWidth /3 ? valDifference : -positionDiff
    }
    carousel.scrollLeft -= positionDiff > firstImgWidth /3 ? valDifference : -positionDiff
}

const dragStart = (e) =>
{
    isDragStart = true
    prevPageX = e.pageX
    prevScrollLeft = carousel.scrollLeft;
}
const dragging = (e) =>
{
    if (!isDragStart) return
    e.preventDefault()
    carousel.classList.add('dragging')
    positionDiff = e.pageX - prevPageX
    carousel.scrollLeft = prevScrollLeft - positionDiff
}
const dragStop = () =>
{
    isDragStart = false
    carousel.classList.remove('dragging')
    autoSlide()

}
carousel.addEventListener('mousedown', dragStart)
carousel.addEventListener('mousemove', dragging)
carousel.addEventListener('mouseup', dragStop)


// anons and ads
const adsH2 = document.querySelectorAll('.sliderMenu h2')[0]
const anonsH2 = document.querySelectorAll('.sliderMenu h2')[1]
const ads = document.querySelector('.ads')
const anons = document.querySelector('.anons')
adsH2.onclick = () =>
{
    anonsH2.classList.remove('active')
    adsH2.classList.add('active')
    anons.classList.add('hide')
    ads.classList.remove('hide')
}
anonsH2.onclick = () =>
{
    adsH2.classList.remove('active')
    anonsH2.classList.add('active')
    anons.classList.remove('hide')
    ads.classList.add('hide')
}


