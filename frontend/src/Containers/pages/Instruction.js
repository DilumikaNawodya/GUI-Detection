import React from "react";

function Instruction() {
  return (
    <div>
      <center>
        <h1>Instructions</h1>
      </center>
      <hr />
      <p>
        The website aims to show the results of an empirical study on Google
        Material Design component design guidelines. The study also proposes an
        UI design smell detector and evaluates it in the Rico dataset. It is a
        gallery to show conformance examples and violation examples from Google
        material design and the Rico dataset.{" "}
      </p>
      <p>
        Each guideline includes ID, name, component type, general design
        dimension, component design aspect, severity, content, needed
        information, conformance example gallery and violation example gallery.{" "}
      </p>
      <p>
        The select list is used to filter guidelines of given classes. These
        four classes are independent and can be combined to filter guidelines.
      </p>
      <p>
        Component Type refers to which component the guideline contains. It has
        backdrop, banner, bottom bar, bottom navigation, bottom sheet, button,
        card, chip, dialog, divider, floating action button(FAB), image list,
        list, navigation drawer, navigation rail, picker, progress indicator,
        side sheet, snackbar, tab, text field, tooltip, and top bar.
      </p>
      <p>
        General Design Dimension is modified from the Google Material Design
        definition. It has animation, color, communication, iconography,
        landscape, layout, navigation, shape, and typography.
      </p>
      <p>
        Component Design Aspect is modified from the Google Material Design
        component hierarchy. It has anatomy, usage, behavior, and placement.
      </p>
      <p>
        Severity has error, warning, and permission. This class will be
        indicated by color.
      </p>
      <p>
        The search bar is used to search ID, name and content. The search
        results and number will be displayed on the page immediately.
      </p>
      <p>
        Some guidelines such as guidelines of backdrop, navigation rail and side
        sheet are in beta, which means they are the latest insights and may
        significantly change in further. These beta rules are indicated by
        Picture failed to load.
      </p>
      <p>
        Needed information refers to the atomic information needed to implement
        this validator. Details of atomic information extractors can be found in
        our paper.
      </p>

      <ul>
        <li>‘Metadata’ refers to metadata extractor.</li>
        <li>‘Color’ refers to color extractor.</li>
        <li>‘Typography’ refers to typography extractor.</li>
        <li>‘Iconography’ refers to iconography extractor.</li>
        <li>
          ‘Animation Effect’ refers to animation information, but these
          guidelines have NOT been implemented in our tool.
        </li>
      </ul>
      <p>
        In the slide show, there is a label with ‘md’ or ‘real’ in the upper
        left corner. This label indicates the corresponding example is from
        Google Material Design or the Rico dataset. Most examples labeled ‘md’
        are synthetic. Examples labeled ‘real’ are screenshots from real-world
        android apps.
      </p>
    </div>
  );
}
export default Instruction;
