import React from "react";


class TodoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {projectName: props.projects[0].id, text: '', creator: props.users[0].id}
    }

    handleSubmit(event){
        console.log(this.state.projectName + ', ' + this.state.text + ', ' + this.state.creator)
        this.props.create_todo(this.state.projectName, this.state.text, this.state.creator)
        event.preventDefault()
    }

    handleChange(event){
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
        console.log(this.state)
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.projects.length && nextProps.users.length) {
            this.setState({projectName: nextProps.projects[0].id, text: '', creator: nextProps.users[0].id})
        }
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>

                <select name="projectName" onChange={(event) => this.handleChange(event)}>
                    {this.props.projects.map((item)=><option value={item.id}>{item.name}</option>)}
                </select>

                <input type="text" name="text" placeholder="text"
                       value={this.state.text} onChange={(event) => this.handleChange(event)}/>

                <select name="creator" onChange={(event) => this.handleChange(event)}>
                    {this.props.users.map((item)=><option value={item.id}>{item.username}</option>)}
                </select>

                <input type="submit" value="Save"/>
            </form>
        );
    }

}

export default TodoForm;