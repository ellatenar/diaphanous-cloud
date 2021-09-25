
// Add event listener for site info popup
const footer = document.querySelector('#footer')
const siteInfo = document.querySelector('#siteInfo')
const info = document.querySelectorAll('.hidden')

const showInfo = () => () => {
    siteInfo.style.visibility = 'visible'
    info.forEach(p => p.style.visibility = 'visible')
}

const hideInfo = () => () => {
    siteInfo.style.visibility = 'hidden'
    info.forEach(p => p.style.visibility = 'hidden')
}

footer.addEventListener('mouseenter', showInfo)
footer.addEventListener('mouseleave', hideInfo)

// Touch-responsive listeners for mobile
footer.addEventListener('touchstart', showInfo)
footer.addEventListener('touchend', hideInfo)
footer.addEventListener('touchcancel', hideInfo)
