import React from 'react'
import {
    Link
} from "react-router-dom";

function NavbarItem({name, href}) {
    return (
        <li >
            <Link to={href}>{name}</Link>
        </li>
    )
}


export default function Navbar({navbarItems}) {
    return (
        <nav >
            <div >
                <ul>
                    {navbarItems.map((item) => <NavbarItem name={item.name} href={item.href}/>)}
                </ul>
            </div>
        </nav>
    )
}

// export default Navbar