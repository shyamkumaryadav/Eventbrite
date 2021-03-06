M.AutoInit()
const sideNav = M.Sidenav.init(document.querySelector(".sidenav"), {})

document.getElementById('openNav').addEventListener('click', (e) => {
    sideNav.open();
})

