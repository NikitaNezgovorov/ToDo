// import logo from './logo.svg';
import './App.css';
import React from 'react';
import {
    Routes,
    Route, BrowserRouter,
} from "react-router-dom";
import axios from 'axios';
import UserList from './components/User';
import ToDoList from './components/ToDo.js';
import Navbar from './components/Menu.js';
import LoginForm from './components/Auth.js';
import {ProjectList} from "./components/Projects";


const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            navbarItems: [
                {name: 'Users', href: '/'},
                {name: 'Projects', href: '/projects'},
                {name: 'TODOs', href: '/todos'},
            ],
            users: [],
            projects: [],
            project: {},
            todos: [],
            auth: {username: '', is_login: false},
        }
    }

    login(username, password) {
        axios.post(get_url('token/'), {username: username, password: password})
            .then(response => {
                const result = response.data
                const access = result.access
                const refresh = result.refresh
                localStorage.setItem('login', username)
                localStorage.setItem('access', access)
                localStorage.setItem('refresh', refresh)
                this.setState({'auth': {username: username, is_login: true}})
                this.load_data()
            }).catch(error => {
            if (error.response.status === 401) {
                alert('Неверный логин или пароль')
            } else {
                console.log(error)
            }
        })
    }


    logout() {
        localStorage.setItem('login', '')
        localStorage.setItem('access', '')
        localStorage.setItem('refresh', '')
        this.setState({'auth': {username: '', is_login: false}})
    }

    load_data() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.state.auth.is_login) {
            const token = localStorage.getItem('access')
            headers['Authorization'] = 'Bearer ' + token
        }

        axios.get(get_url('users/'), {headers})
            .then(response => {
                //console.log(response.data)
                this.setState({users: response.data})
            }).catch(error =>

            console.log(error)
        )

        axios.get(get_url('projects/'), {headers})
            .then(response => {
                //console.log(response.data)
                this.setState({projects: response.data.results})
            }).catch(error =>
            console.log(error)
        )

        axios.get(get_url('todos/'), {headers})
            .then(response => {
                //console.log(response.data)
                this.setState({todos: response.data.results})
            }).catch(error =>
            console.log(error)
        )
    }


    componentDidMount() {
        const username = localStorage.getItem('login')
        if ((username !== "") && (username != null)) {
            this.setState({'auth': {username: username, is_login: true}}, () => this.load_data())
        }
    }


    render() {
        return (
            <BrowserRouter>
                <header>
                    <Navbar navbarItems={this.state.navbarItems} auth={this.state.auth}
                            logout={() => this.logout()}/>
                </header>
                <main role='main'>
                    <div>
                        <Routes>
                            <Route exact path='/' element={<UserList users={this.state.users}/>}/>
                            <Route exact path='/todos' element={<ToDoList items={this.state.todos}/>}/>
                            <Route path='/projects' element={<ProjectList items={this.state.projects}/>}/>
                            <Route path='/login' element={<LoginForm
                                login={(username, password) => this.login(username, password)}/>}/>
                            {/*<Route path="/project/:id"*/}
                            {/*       element={<ProjectDetail getProject={(id) => this.getProject(id)}*/}
                            {/*                               item={this.state.project}/>}/>*/}


                        </Routes>
                    </div>
                </main>
            </BrowserRouter>


        )
    }


    // getProject(id) {
    //     let headers = {
    //         'Content-Type': 'application/json'
    //     }
    //     console.log(this.state.auth)
    //     if (this.state.auth.is_login) {
    //         const token = localStorage.getItem('access')
    //         headers['Authorization'] = 'Bearer ' + token
    //     }
    //
    //     axios.get(get_url(`projects/${id}`), {headers})
    //         .then(response => {
    //             this.setState({project: response.data})
    //         }).catch(error => console.log(error))
    // }
}


export default App;


