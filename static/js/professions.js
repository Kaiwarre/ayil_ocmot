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


