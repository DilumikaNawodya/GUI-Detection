import { Container } from "@material-ui/core";
import React from "react";
import ReportContainer from "../../Components/Report/reportcontainer";
import { data } from "./GuidelineData";

function ReportPage() {
  const violatedIds = JSON.parse(localStorage.getItem("violatedIds"));

  const violatedIdSet = new Set(violatedIds["violated_ids"]);

  const datas = data.filter((a) => violatedIdSet.has(a.id));

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
