import { Container } from "@material-ui/core";
import React from "react";
import ReportContainer from "../../Components/Report/reportcontainer";
import { data } from "./GuidelineData";

function ReportPage() {
  const violatedIds = new Set(JSON.parse(localStorage.getItem("violatedIds")));

  const datas = data.filter((a) => violatedIds.has(a.id));

  return (
    <Container>
      <center>
        <h1> Report Page </h1>
      </center>
      <hr />
      {datas.map((item, index) => {
        return <ReportContainer data={item} />;
      })}
    </Container>
  );
}

export default ReportPage;
