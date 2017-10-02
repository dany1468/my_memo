import types from '../constants/';

export const initialState = {
  todos: [],
  lastDeletedTodo: {},
};

export const reducer = (state = initialState, action) => {
  switch (action.type) {

    case types.SUBMIT_TODO:
      return {
        ...state,
        todos: [
          ...state.todos,
          {
            id: action.id,
            text: action.text,
          },
        ],
      };

    case types.DELETE_TODO:
      return {
        ...state,
        todos: [
          ...state.todos.filter(todo => (
            todo.id !== action.id
          )),
        ],
        lastDeletedTodo: state.todos.find(todo => (
          todo.id === action.id
        )),
      };

    case types.UNDELETE_TODO:
      return {
        ...state,
        todos: [
          ...state.todos,
          state.lastDeletedTodo,
        ],
        lastDeletedTodo: {},
      };
    default:
      return state;
  }
};

export default reducer;
