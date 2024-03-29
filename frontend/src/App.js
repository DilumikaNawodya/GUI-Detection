import React from "react";
import { BrowserRouter } from "react-router-dom";
import { Switch } from "react-router-dom";
import Layout from "./Containers/layout";
import Home from "./Containers/pages/Home";
import ImagePage from "./Containers/pages/ImagePage";
import ReportPage from "./Containers/pages/ReportPage";
import GuidelinePage from "./Containers/pages/GuidelinePage";
import Instruction from "./Containers/pages/Instruction";
import { allRoutes } from "./routes";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <allRoutes.PublicRoutes exact path="/">
            <Layout main={<Home />} />
          </allRoutes.PublicRoutes>

          <allRoutes.PublicRoutes exact path="/report-page">
            <Layout main={<ReportPage />} />
          </allRoutes.PublicRoutes>

          <allRoutes.PublicRoutes exact path="/guideline-page">
            <Layout main={<GuidelinePage />} />
          </allRoutes.PublicRoutes>

          <allRoutes.PublicRoutes exact path="/image-page">
            <Layout main={<ImagePage />} />
          </allRoutes.PublicRoutes>

          <allRoutes.PublicRoutes exact path="/instructions">
            <Layout main={<Instruction />} />
          </allRoutes.PublicRoutes>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
