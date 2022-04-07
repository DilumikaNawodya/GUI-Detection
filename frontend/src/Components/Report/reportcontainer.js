import { Card, CardContent, Grid, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/styles";
import React from "react";
import CheckCircleIcon from '@material-ui/icons/CheckCircle';
import CancelIcon from '@material-ui/icons/Cancel';
import Chip from '@material-ui/core/Chip';


const useStyles = makeStyles((theme)=> ({
    main: {
        marginTop: "20px"
    }
}))


function ReportContainer({data}){

    const classes = useStyles()

    return(
        <div class={classes.main}>
            <Card>
                <CardContent>
                    <Grid container spacing={6}>
                        <Grid item lg={4}>
                            <Grid container>
                                {data.status && <CheckCircleIcon style={{ color: "green", marginBlock: "auto", marginRight: "10px"}}/>}
                                {!data.status && <CancelIcon style={{ color: "red", marginBlock: "auto", marginRight: "10px"}}/>}
                                <h1>{data.title}</h1><br/>
                            </Grid>

                            <Chip size="small" label={data.path[0]} style={{ color: "blue", marginBlock: "auto", marginRight: "10px"}}/>
                            <Chip size="small" label={data.path[1]} style={{ color: "blue", marginBlock: "auto", marginRight: "10px"}}/>
                            <Chip size="small" label={data.path[2]} style={{ color: data.status ? "green": "red" , marginBlock: "auto", marginRight: "10px"}}/>
                        
                            
                            {data.content.map((item, index)=>(
                                <>
                                    <h4>{item.title}</h4>
                                    <>{item.subcontent.map((subitem, subindex) => <Chip size="small" label={subitem} style={{ margin: "5px"}}/>)}</>
                                </>
                            ))}

                        </Grid>
                        <Grid item lg={4}>
                            <img src={data.ok_image} height="400px"/> <br/>
                        </Grid>
                        <Grid item lg={4}>
                            <img src={data.notok_image} height="400px"/>
                        </Grid>
                    </Grid>
                </CardContent>
            </Card>
        </div>
            
    )
}

export default ReportContainer