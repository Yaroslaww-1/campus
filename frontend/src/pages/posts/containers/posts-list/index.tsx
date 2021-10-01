import { useEffect } from "react";
import { observer } from "mobx-react-lite";

import { postsState, PostsState } from "../../posts.state";

import { PageComponent } from "@components/index";
import { PostComponent } from "@pages/posts/components/post";

interface IProps {
  state: PostsState;
}

const PostsListContainerContent: React.FC<IProps> = observer(({ state }) => {
  useEffect(() => {
    state.fetchPosts();
  }, []);

  return (
    <PageComponent>
      {state.posts.map(post => <PostComponent key={post.id} post={post} />)}
    </PageComponent>
  );
});

export const PostsListContainer: React.FC = () => (
  <PostsListContainerContent state={postsState} />
);
