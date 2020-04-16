import React, {Component} from 'react'
import {Redirect} from 'react-router-dom'

// HomePage
import HomePage from '../components/DashboardStudent/StudentHome'


// Nav
import Nav from '../components/NavBar'




class StudentHome extends Component{

    state={
        logout:false,
        changePassword:false
    }

    changePassword=()=>{
        console.log('changepwd')
        this.setState({
            changePassword:true
        })
    };

    onLogout=()=>{
        console.log('here')
        this.setState({
            logout:true
        })
    }

    render(){

      
        return(
            <Nav
                user="Student"
                onLogout={this.onLogout}
                changePassword={this.changePassword}
            >
                <HomePage />
            {this.state.changePassword===true?<Redirect to='/changepassword' />:null}
            {this.state.logout===true?<Redirect to='/login' />:null}

            </Nav>
        )
    }
}

export default StudentHome