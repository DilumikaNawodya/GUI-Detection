import { Card, CardContent, Grid } from "@material-ui/core";
import { makeStyles } from "@material-ui/styles";
import React from "react";
import Chip from "@material-ui/core/Chip";

const useStyles = makeStyles((theme) => ({
  main: {
    marginTop: "20px",
  },
}));

function ReportContainer({ data }) {
  const classes = useStyles();

  return (
    <div class={classes.main}>
      <Card>
        <CardContent>
          <Grid container spacing={6}>
            <Grid item lg={4}>
              <Grid container>
                <h1>{data.title}</h1>
                <br />
              </Grid>

              <Chip
                size="small"
                label={data.path[0]}
                style={{
                  color: "blue",
                  marginBlock: "auto",
                  marginRight: "10px",
                }}
              />
              <Chip
                size="small"
                label={data.path[1]}
                style={{
                  color: "blue",
                  marginBlock: "auto",
                  marginRight: "10px",
                }}
              />
              <Chip
                size="small"
                label={data.path[2]}
                style={{
                  color: data.status ? "green" : "red",
                  marginBlock: "auto",
                  marginRight: "10px",
                }}
              />
              <p>{data.content}</p>
            </Grid>
            <Grid item lg={4}>
              <img src={data.ok_image} height="400px" alt="Correct" /> <br />
            </Grid>
            <Grid item lg={4}>
              <img src={data.notok_image} height="400px" alt="Incorrect" />
            </Grid>
          </Grid>
        </CardContent>
      </Card>
    </div>
  );
}

export default ReportContainer;
