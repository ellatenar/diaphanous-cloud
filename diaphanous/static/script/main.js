
// Add event listener for site info popup
const footer = document.querySelector('#footer')
const siteInfo = document.querySelector('#siteInfo')
const info = document.querySelectorAll('.hidden')


footer.addEventListener('mouseenter', () => {
    siteInfo.style.visibility = 'visible'
    info.forEach(p => p.style.visibility = 'visible')

})

footer.addEventListener('mouseleave', () => {
    siteInfo.style.visibility = 'hidden'
    info.forEach(p => p.style.visibility = 'hidden')
})