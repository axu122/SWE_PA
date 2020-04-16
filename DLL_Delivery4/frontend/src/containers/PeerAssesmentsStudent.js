import React, {Component} from 'react'
import Moment from 'moment'

// HomePage
import Assesments from '../components/DashboardStudent/Assesments'
import ToDOModal from '../components/DashboardStudent/SubmitModal'


// Nav
import Nav from '../components/NavBar'

// redirect
import {Redirect} from 'react-router-dom'


const assesmentsToDo=[
    {
        name:'Delivery 6 Assesments',
        teamMates:['Pedro', 'John', 'Adam'],
        dueDate: new Date(),
        id:12312
    }
]

const assesmentsClosed=[
    {
        name:'Delivery 5 Assesments',
        teamMates:['Pedro', 'John', 'Adam'],
        dueDate: Moment(new Date()).subtract(10, 'days').calendar(),
        id:12312
    }
]



class StudentHome extends Component{

    state={
        openToDoModal:false,
        todoSelected:null,
        todoResponses:null,
        logout:false,
        changePassword:false
    }


    // *----------HANDLE MODAL METHODS------------------*
     openModalHandler = (e) => {
         console.log(assesmentsToDo[e])
        this.setState({
            openToDoModal:true,
            todoSelected:assesmentsToDo[e]

        });
      };
    
    handleClose = () => {
        this.setState({
            openToDoModal:false
        })
      };

    changePassword=()=>{
        console.log('changepwd')
        this.setState({
            changePassword:true
        })
    };

    // LOGOUT
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
                <Assesments
                toDoArr={assesmentsToDo}
                closedArr={assesmentsClosed}
                openModal={this.openModalHandler}
                />

            <ToDOModal 
                close={this.handleClose}
                open={this.state.openToDoModal}
                info={this.state.todoSelected}
            />
            {this.state.changePassword===true?<Redirect to='/changepassword' />:null}
            {this.state.logout===true?<Redirect to='/login' />:null}

            </Nav>
        )
    }
}

export default StudentHome