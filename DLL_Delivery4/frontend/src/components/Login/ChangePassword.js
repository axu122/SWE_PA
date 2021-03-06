import React from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Paper from '@material-ui/core/Paper';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Hidden from '@material-ui/core/Hidden';
import StudyingStudent from '../../Assets/professorLogin.svg'

function Copyright() {
    return (
      <Typography variant="body2" color="textSecondary" align="center">
         Boston College

        {new Date().getFullYear()}
        {'.'}
      </Typography>
    );
  }

const useStyles = makeStyles(theme => ({

  image: {
    backgroundImage: StudyingStudent,
    backgroundRepeat: 'no-repeat',
    // backgroundColor:
    //   theme.palette.type === 'dark' ? theme.palette.grey[900] : theme.palette.grey[50],
    backgroundSize: 'cover',
    backgroundPosition: 'center',
  },
  paper: {
    margin: theme.spacing(8, 4),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: '#6C63FF',
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
  back: {
    margin: theme.spacing(1, 0, 2),
  },
}));

export default function SignInSide(props) {
  const classes = useStyles();

  return (
    <Grid container component="main" className={classes.root}>
      {/* <CssBaseline /> */}
      <Hidden smDown  >
          <Grid item  md={7} >
            <img src={StudyingStudent} alt='studying' style={{width:'120vh'}}/>

          </Grid>
      </Hidden>
      <Grid item xs={12} sm={12} md={5} component={Paper} elevation={6} square>
        <div className={classes.paper}>
          <Avatar className={classes.avatar}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Change Password
          </Typography>
          <form className={classes.form} noValidate onSubmit={props.changePasswordHandler}>
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="currentPassword"
              label="Current Password"
              type="password"
              name="currentPassword"
              autoComplete="currentPassword"
              autoFocus
              onChange={props.textHandler}

            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="newPassword"
              label="New password"
              type="password"
              id="newPassword"
              autoComplete="newPassword"
              onChange={props.textHandler}

            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="confirmPassword"
              label="Confirm password"
              type="password"
              id="confirmPassword"
              autoComplete="confirmPassword"
              onChange={props.textHandler}

            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
              disabled={props.currentPassword!==null && props.pass!==null?false:true}
              onClick={props.changePasswordHandler}
            >
              Confirm Change
            </Button>

            <Button
              type="submit"
              fullWidth
              variant="outlined"
              color="primary"
              className={classes.back}
              onClick={props.handleBack}
            >
              Back To Home
            </Button>

            <Box mt={5}>
                {Copyright}
            </Box>
          </form>
        </div>
      </Grid>
    </Grid>
  );
}