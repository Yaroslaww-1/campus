import { useEffect } from "react";
import { observer } from "mobx-react-lite";

import { postsState, PostsState } from "./posts.state";

import { PageComponent } from "@components/index";

interface IProps {
  state: PostsState;
}

const PostsPageContent: React.FC<IProps> = observer(({ state }) => {
  useEffect(() => {
    state.fetchPosts();
  }, []);

  return (
    <PageComponent>
      {state.posts.map(post => <p key={post.id}>{post.id} - {post.name}</p>)}
    </PageComponent>
  );
});

export const PostsPage: React.FC = () => (
  <PostsPageContent state={postsState} />
);
