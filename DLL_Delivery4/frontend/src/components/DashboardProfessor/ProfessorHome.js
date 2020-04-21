import React from 'react'

import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card'
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActionArea';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

import Icon from '@material-ui/core/Icon';
import CheckCircleRoundedIcon from '@material-ui/icons/CheckCircleRounded';
import ErrorRoundedIcon from '@material-ui/icons/ErrorRounded';
import ListRoundedIcon from '@material-ui/icons/ListRounded';
import TimelineRoundedIcon from '@material-ui/icons/TimelineRounded';
import VisibilityRoundedIcon from '@material-ui/icons/VisibilityRounded';
import ClearRoundedIcon from '@material-ui/icons/ClearRounded';




const ProfessorHome = props=>{

    let classSelect;
    if(props.classes.length>0){
        classSelect=props.classes.map((e,i)=>(
            <Grid item xs={12} md={6} sm={6} key={e.id}>
                <Card>
                    <CardActions onClick={()=>props.selectClass(i)}>
                    <CardContent style={{display:'flex', alignItems:'flex-start', flexDirection:'column'}}>
                        <Typography variant='h5'> <b>{e.name}</b> </Typography>
                        <Typography variant='subtitle1'> <b>Teams: </b> {e.teams}</Typography>
                        <Typography variant='subtitle2'> Click To See Class </Typography>
                    </CardContent>
                    </CardActions>

                </Card>
            </Grid>

        ))
    }
    if(props.classes.length===0){
        toDoArr=(
            <Grid item xs={12} md={4} sm={6}>


                <Typography variant='subtitle1' > No Assessments in the to grade!</Typography>

            </Grid>

        )
    }

// 
    return(
        <Grid container spacing={6}>

            <Grid item sm={10} xs={10}>
                <Typography variant="h4">
                    Welcome Professor
                </Typography>
            </Grid>

            <Grid item container sm={12} xs={12} spacing={6} style={{display:'flex',justifyContent:'space-between'}}>
                
                {classSelect}

            </Grid>


        </Grid>
    )
}

export default ProfessorHome