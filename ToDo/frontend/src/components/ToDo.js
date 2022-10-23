import React from 'react';

const ToDoListItem = ({item, delete_todo}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.text}</td>
            <td>{item.createDate}</td>
            <td>{item.projectName}</td>
            <td>{item.creator}</td>
            <td>
                <button onClick={() => delete_todo(item.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const ToDoList = ({items, delete_todo}) => {
    //console.log(users)
    return (
        <table className="table">
            <tr>
                <th>Id</th>
                <th>Text</th>
                <th>Create</th>
                <th>Project</th>
                <th>Creator</th>
            </tr>
            {items.map((item) => <ToDoListItem item={item} delete_todo={delete_todo}/>)}

        </table>
    )
}

export default ToDoList