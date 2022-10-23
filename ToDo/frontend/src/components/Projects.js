import React from 'react'
import {Link, useParams} from "react-router-dom";


const ProjectListItem = ({item, delete_project}) => {
    let link_to = `/projects/${item.id}`
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.repository}</td>
            <td>
                <button onClick={() => delete_project(item.id)} type='button'>Delete</button>
            </td>

            <td><Link to={link_to}>Detail</Link></td>
        </tr>
    )
}

const ProjectList = ({items, delete_project}) => {
    return (
        <table className="table">
            <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Repository</th>
                <th></th>
            </tr>
            {items.map((item) => <ProjectListItem item={item} delete_project={delete_project}/>)}
        </table>
    )
}

const ProjectUserItem = ({item}) => {

    return (
        <li>
            {item.username} {item.email}
        </li>
    )
}


const ProjectDetail = ({item, users}) => {
    let {projectId} = useParams();
    console.log(item)
    let filtered_item = item.filter((project => project.id === parseInt(projectId)))
    console.log(filtered_item)
    let projectUsersId = filtered_item[0].users ? filtered_item[0].users : []
    let projectUsers = users.filter(user => projectUsersId.includes(user.id))
    // console.log(id)
    return (
        <div>
            <h1>{filtered_item[0].name}</ h1>
            Repository: <a href={filtered_item[0].repository}>{filtered_item[0].repository}</a>
            <p></p>
            Users:
            <ol>
                {projectUsers.map((users) => <ProjectUserItem item={users}/>)}
            </ol>
        </div>
    )

}

export {ProjectList, ProjectDetail}