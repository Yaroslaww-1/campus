import { PageComponent } from "@components/index";
import { PostsListContainer } from "./containers/posts-list";

export const PostsPage: React.FC = () => {
  return (
    <PageComponent>
      <PostsListContainer />
    </PageComponent>
  );
};
