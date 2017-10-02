/* global expect, it, describe */

import React from 'react';
import { shallow } from 'enzyme';
import UndeleteTodo from '.';

describe('AddTodo component', () => {
  let component;
  const undeleteMock = jest.fn();

  beforeEach(() => {
    component = shallow(
      <UndeleteTodo
        undeleteTodo={undeleteMock}
        lastDeletedTodo={{}}
      />,
    );
  });

  it('Should render successfully', () => {
    expect(component.exists()).toEqual(true);
  });

  describe('Undelete todo button', () => {
    it('Should exist', () => {
      expect(component.find('.todo-undelete').length).toEqual(1);
    });

    it('Should call the undeleteTodo function when clicked', () => {
      expect(undeleteMock.mock.calls.length).toEqual(0);
      component.find('.todo-undelete').simulate('click');
      expect(undeleteMock.mock.calls.length).toEqual(1);
    });
  });
});
