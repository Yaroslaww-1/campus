/* eslint-disable react/display-name */
import React, { Component } from "react";

import { OneTable } from "./OneTable";
import { observer } from "mobx-react";

export const AllTable = observer(class extends Component{
  constructor(props: Array<object>[]) {
    super(props);       
  };
  render() { 
    return (
      <div className="allTables">
        <h1>Перший тиждень</h1>
        <OneTable/>
        <h1>Другий тиждень</h1>
        <OneTable/>
      </div>
    );
  }
});
