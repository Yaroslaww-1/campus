import { Provider } from "mobx-react";

import { AllTable } from "./comp/AllTable";

import scheduleStore from "./stores/scheduleStore";

const stores = {
  scheduleStore,
};
export const SchedulePage: React.FC = () => (
  <Provider {...stores}>
    <AllTable />
  </Provider>
);

export default  SchedulePage;