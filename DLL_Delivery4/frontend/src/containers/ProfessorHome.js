import React, {Component} from 'react'
import {Redirect} from 'react-router-dom'

// HomePage
import HomePage from '../components/DashboardProfessor/ProfessorHome'


// Nav
import Nav from '../components/NavBar'




class ProfessorHome extends Component{

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
                changePassword={this.changePassword}
                onLogout={this.onLogout}
            >
                <HomePage />
            {this.state.changePassword===true?<Redirect to='/changepassword' />:null}
            {this.state.logout===true?<Redirect to='/login' />:null}

            </Nav>
        )
    }
}

export default ProfessorHome