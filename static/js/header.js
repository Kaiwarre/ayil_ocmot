const btnClose = document.getElementById('closeHeader')
const headerEnd = document.querySelector('.headerEnd')
const activeBtn = document.querySelector('.Active')
btnClose.onclick = () =>
{
    headerEnd.classList.add('hide')
}
activeBtn.onclick = (e) =>
{
    e.preventDefault()
    headerEnd.classList.remove('hide')
}


