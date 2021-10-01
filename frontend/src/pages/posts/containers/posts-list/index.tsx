import { useEffect } from "react";
import { observer } from "mobx-react-lite";

import { postsState, PostsState } from "../../posts.state";

import { PageComponent } from "@components/index";
import { PostsListComponent } from "@pages/posts/components/posts-list";

interface IProps {
  state: PostsState;
}

const PostsListContainerContent: React.FC<IProps> = observer(({ state }) => {
  useEffect(() => {
    state.fetchPosts();
  }, []);

  return (
    <PageComponent>
      <PostsListComponent posts={state.posts} />
    </PageComponent>
  );
});

export const PostsListContainer: React.FC = () => (
  <PostsListContainerContent state={postsState} />
);
