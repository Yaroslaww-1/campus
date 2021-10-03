import { PageComponent } from "@components/index";
import { PostsListContainer } from "./containers/posts-list";

import styles from "./styles.module.scss";

export const PostsPage: React.FC = () => {
  return (
    <PageComponent classes={{ root: styles.root }}>
      <PostsListContainer />
    </PageComponent>
  );
};
