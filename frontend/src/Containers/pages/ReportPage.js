import { Container } from "@material-ui/core";
import React from "react";
import ReportContainer from "../../Components/Report/reportcontainer";
import { data } from "./ReportData";


function ReportPage(){

    const datas = data

    return(
        <Container>

            <center><h1> Report Page </h1></center>
            <hr/>
            {datas.map((item, index)=>{
                return(
                    <ReportContainer data={item}/>
                )
            })}
        </Container>
    )
}

export default ReportPage