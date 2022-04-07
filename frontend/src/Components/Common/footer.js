import React from "react";
import { CssBaseline } from "@material-ui/core";
import { Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core";
import { Container } from "@material-ui/core";
import { Link } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    flexDirection: "column",
    minHeight: "auto",
    position: "absolute",
    left: 0,
    bottom: 0,
    right: 0,
  },
  main: {
    marginTop: theme.spacing(3),
    marginBottom: theme.spacing(2),
  },
  footer: {
    padding: theme.spacing(2, 2),
    marginTop: "calc(5%)",
    backgroundColor:
      theme.palette.type === "light"
        ? theme.palette.grey[200]
        : theme.palette.grey[800],
  },
}));

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary">
      {"Copyright © "}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

export default function Footer() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <CssBaseline />
      <Container component="main" className={classes.main} maxWidth="sm" />
      <footer className={classes.footer}>
        <Container maxWidth="sm">
          <Typography variant="body1">
            <Copyright />
          </Typography>
        </Container>
      </footer>
    </div>
  );
}
