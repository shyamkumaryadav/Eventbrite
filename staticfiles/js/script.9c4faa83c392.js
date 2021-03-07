M.AutoInit()
const sideNav = M.Sidenav.init(document.querySelector(".sidenav"), {})
var elems = document.querySelectorAll('.modal');
var instances = M.Modal.init(elems, {
    dismissible:false,
    opacity: 0.9
});
document.getElementById('openNav').addEventListener('click', (e) => {
    sideNav.open();
})

