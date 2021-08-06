const mobNav = document.querySelector('#mobNav');
const Header = document.querySelector('#header');
const mainSection = document.querySelector('main');
console.dir(mainSection);

const openMenu = ()=>{
    mobNav.classList.toggle('show-mob-nav');
}

const closeMenu = () =>{
    mobNav.classList.toggle('show-mob-nav');
}

document.addEventListener('scroll', ()=>{
    let position = mainSection.getBoundingClientRect(); 
    
    if(position.top < 0){
        Header.classList.add("changeNavBg");
    }
    else{
        Header.classList.remove("changeNavBg");
    }
})