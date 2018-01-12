# -*- coding: latin-1 -*-
# - HTML Page Code



hi_test = 'hi hi hi'


edit_people = '''<style>

.input_form_wrap { display: inline-block; vertical-align: top; border: 15px dashed #839496; padding: 20px; margin: 5px; }

</style>
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
<style>
.people_list_wrap { display: inline-block; }
.people_list_item { margin: 10px; padding: 20px; border: 5px solid #eee; padding-right: 15px; transition: border 1s; display: inline-block; width: 100px; }
.people_list_item:hover { border: 5px solid #839496; }

.chat_link { font-size: 12px; padding-left: 15px; }
.chat_link a { color: #aaa; }

</style>
<div class="people_list_wrap">
<input type="text" ng-model="chat" />
  <div class="people_list_data">
    <div class="people_list_item" ng-repeat="item in people_list">
      <div>[! item.item_name !]</div>
      <div class="chat_link"><a href="https://[!chat!].com/[! item.item_chat !]" target="_blank">[! item.item_chat !]</a></div>
    </div><!-- . people_list_item - -->
  </div><!-- . people_list_data - -->
</div><!-- . people_list_wrap - -->

  
</div><!-- . main_html - -->

'''
