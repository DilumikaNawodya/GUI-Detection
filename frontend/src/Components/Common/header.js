import React from "react";
import { makeStyles } from "@material-ui/core";
import { AppBar } from "@material-ui/core";
import { Toolbar } from "@material-ui/core";
import { Typography } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
  high: {
    fontWeight: "900",
  },
  low: {
    fontWeight: "100",
  },
  headerColor: {
    backgroundColor: "#28282B",
  },
}));

export default function Header() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static" className={classes.headerColor}>
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            Createaro
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}
