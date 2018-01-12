# -*- coding: latin-1 -*-
# - HTML Page Code



hi_test = 'hi hi hi'


edit_people = '''


<div class="main_html">

<div class="input_button" ng-hide="show_input=='on'" ng-click="showInput()">Show Input</div>
<div class="input_button" ng-hide="show_input=='off'" ng-click="hideInput()">Hide</div>
<div class="input_form_wrap" ng-show="show_input=='on'">
  <form action="../../_add_person" method="post">
    <table>
      <tr>
        <td class="label">Name</td>
        <td class="input"><input type="text" name="item_name" /></td>
      </tr>
      <tr>
        <td class="label">Inst</td>
        <td class="input"><input type="text" name="item_inst" /></td>
      </tr>
      <tr>
        <td class="label">Twit</td>
        <td class="input"><input type="text" name="item_twit" /></td>
      </tr>
      <tr>
        <td class="label">Chat</td>
        <td class="input"><input type="text" name="item_chat" /></td>
      </tr>
      <tr>
        <td class="label">Year</td>
        <td class="input"><input type="text" name="item_year" /></td>
      </tr>
      <tr>
        <td class="label">Loca</td>
        <td class="input"><input type="text" name="item_loca" /></td>
      </tr>
      <tr>
        <td class="label">Orig</td>
        <td class="input"><input type="text" name="item_orig" /></td>
      </tr>
      <tr>
        <td class="label">Type</td>
        <td class="input"><input type="text" name="item_type" /></td>
      </tr>
      <tr>
        <td class="label">Kind</td>
        <td class="input"><input type="text" name="item_kind" /></td>
      </tr>
      <tr>
        <td> </td>
        <td class="submit"><input type="submit" value="Add Person" /></td>
      </tr>
    </table>
  </form>
</div><!-- . input_form_wrap - -->

<div class="people_list_wrap">
  <div class="people_list_data">
    <div class="people_list_item" ng-repeat="item in people_list">
      <div>[!item.item_name!]</div>
    </div><!-- . people_list_item - -->
  </div><!-- . people_list_data - -->
</div><!-- . people_list_wrap - -->

  
</div><!-- . main_html - -->

'''
