<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.10.0-A Coruña" simplifyMaxScale="1" readOnly="0" simplifyAlgorithm="0" styleCategories="LayerConfiguration|Symbology|Labeling|Fields|Forms|MapTips|Rendering|CustomProperties|GeometryOptions" labelsEnabled="0" simplifyLocal="1" simplifyDrawingTol="1" minScale="0" simplifyDrawingHints="1" hasScaleBasedVisibilityFlag="0" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="RuleRenderer" forceraster="0" enableorderby="0" symbollevels="0">
    <rules key="{abd91421-ad1a-486d-afef-682f9eae3f40}">
      <rule key="{423e6e34-9776-40b5-bc12-721bc115325d}" label="as van de weg" symbol="0" filter=" &quot;versieIMRO&quot; in ( 'IMRO2008' ,  'IMRO2012' ) and  &quot;naam&quot; = 'as van de weg'"/>
      <rule key="{70746590-e588-4fb8-b319-6e66d9ffea6a}" label="dwarsprofiel" symbol="1" filter=" &quot;versieIMRO&quot; in ( 'IMRO2008' ,  'IMRO2012' ) and  &quot;naam&quot; = 'dwarsprofiel'"/>
      <rule key="{3e072460-1a7e-4fb9-974c-993b3bbf8167}" label="gevellijn" symbol="2" filter=" &quot;versieIMRO&quot; in ( 'IMRO2008' ,  'IMRO2012' ) and  &quot;naam&quot; = 'gevellijn'"/>
      <rule key="{aa55eff3-4e64-49bc-914c-bf9997d59c0a}" label="hartlijn leiding" symbol="3" filter=" &quot;versieIMRO&quot; in ( 'IMRO2008' ,  'IMRO2012' ) and  &quot;naam&quot; = 'hartlijn leiding'"/>
      <rule key="{52fd273a-0149-4cc3-af5d-6934fdee0a35}" label="relatie" symbol="4" filter=" &quot;versieIMRO&quot; in ( 'IMRO2008' ,  'IMRO2012' ) and  &quot;naam&quot; = 'relatie'"/>
      <rule key="{fb7e8b95-706f-4469-ae95-ed87e689ca29}" label="as van de weg" symbol="5" filter=" &quot;versieIMRO&quot; = 'IMRO2006' and  &quot;naam&quot; = 'as van de weg'"/>
      <rule key="{a8a77618-3038-487b-8001-9f9c25c71445}" label="dwarsprofiel" symbol="6" filter=" &quot;versieIMRO&quot; = 'IMRO2006' and  &quot;naam&quot; = 'dwarsprofiel'"/>
      <rule key="{ec650e53-edcb-493a-90af-483eb6be46ee}" label="gevellijn" symbol="7" filter=" &quot;versieIMRO&quot; = 'IMRO2006' and  &quot;naam&quot; = 'gevellijn'"/>
      <rule key="{ec62cce6-a610-49de-bd08-69b0e76a718d}" label="hartlijn leiding" symbol="8" filter=" &quot;versieIMRO&quot; = 'IMRO2006' and  &quot;naam&quot; = 'hartlijn leiding'"/>
      <rule key="{128315eb-079e-4b71-b177-23cbcd46d713}" label="relatie" symbol="9" filter=" &quot;versieIMRO&quot; = 'IMRO2006' and  &quot;naam&quot; = 'relatie'"/>
      <rule key="{0a00be24-9b60-4270-a5ba-b7587742a9ec}" label="anders" symbol="10" filter="ELSE"/>
    </rules>
    <symbols>
      <symbol type="line" force_rhr="0" name="0" alpha="1" clip_to_extent="1">
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="customdash" v="6;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="153,153,153,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="1"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" force_rhr="0" name="1" alpha="1" clip_to_extent="1">
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="customdash" v="1"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,0,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="2"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" force_rhr="0" name="10" alpha="1" clip_to_extent="1">
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="1"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,255,255,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="3"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" force_rhr="0" name="2" alpha="1" clip_to_extent="1">
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="customdash" v="6;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,0,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="2"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" force_rhr="0" name="3" alpha="1" clip_to_extent="1">
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="customdash" v="1"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,0,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="2"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" force_rhr="0" name="4" alpha="1" clip_to_extent="1">
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="customdash" v="1"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,0,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="3"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" force_rhr="0" name="5" alpha="1" clip_to_extent="1">
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="6;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="153,153,153,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="1"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" force_rhr="0" name="6" alpha="1" clip_to_extent="1">
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="1"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,0,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="2"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" force_rhr="0" name="7" alpha="1" clip_to_extent="1">
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="6;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,0,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="2"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" force_rhr="0" name="8" alpha="1" clip_to_extent="1">
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="1"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,0,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="2"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" force_rhr="0" name="9" alpha="1" clip_to_extent="1">
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="1"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,0,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="3"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="fid">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="aanduiding">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="artikelnummer">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="bestemmingsvlak">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="historisch">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="identificatie">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="naam">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="plangebied">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="planstatus">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="symboolcode">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="typePlan">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="versieIMRO">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="verwijzingNaarIllustratie">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="verwijzingNaarObjectgerichteTekst">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="verwijzingNaarTekst">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="dossierID">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="dossierStatus">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="datum">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" name="" field="fid"/>
    <alias index="1" name="" field="aanduiding"/>
    <alias index="2" name="" field="artikelnummer"/>
    <alias index="3" name="" field="bestemmingsvlak"/>
    <alias index="4" name="" field="historisch"/>
    <alias index="5" name="" field="identificatie"/>
    <alias index="6" name="" field="naam"/>
    <alias index="7" name="" field="plangebied"/>
    <alias index="8" name="" field="planstatus"/>
    <alias index="9" name="" field="symboolcode"/>
    <alias index="10" name="" field="typePlan"/>
    <alias index="11" name="" field="versieIMRO"/>
    <alias index="12" name="" field="verwijzingNaarIllustratie"/>
    <alias index="13" name="" field="verwijzingNaarObjectgerichteTekst"/>
    <alias index="14" name="" field="verwijzingNaarTekst"/>
    <alias index="15" name="" field="dossierID"/>
    <alias index="16" name="" field="dossierStatus"/>
    <alias index="17" name="" field="datum"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" expression="" field="fid"/>
    <default applyOnUpdate="0" expression="" field="aanduiding"/>
    <default applyOnUpdate="0" expression="" field="artikelnummer"/>
    <default applyOnUpdate="0" expression="" field="bestemmingsvlak"/>
    <default applyOnUpdate="0" expression="" field="historisch"/>
    <default applyOnUpdate="0" expression="" field="identificatie"/>
    <default applyOnUpdate="0" expression="" field="naam"/>
    <default applyOnUpdate="0" expression="" field="plangebied"/>
    <default applyOnUpdate="0" expression="" field="planstatus"/>
    <default applyOnUpdate="0" expression="" field="symboolcode"/>
    <default applyOnUpdate="0" expression="" field="typePlan"/>
    <default applyOnUpdate="0" expression="" field="versieIMRO"/>
    <default applyOnUpdate="0" expression="" field="verwijzingNaarIllustratie"/>
    <default applyOnUpdate="0" expression="" field="verwijzingNaarObjectgerichteTekst"/>
    <default applyOnUpdate="0" expression="" field="verwijzingNaarTekst"/>
    <default applyOnUpdate="0" expression="" field="dossierID"/>
    <default applyOnUpdate="0" expression="" field="dossierStatus"/>
    <default applyOnUpdate="0" expression="" field="datum"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" field="fid" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="aanduiding" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="artikelnummer" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="bestemmingsvlak" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="historisch" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="identificatie" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="naam" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="plangebied" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="planstatus" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="symboolcode" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="typePlan" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="versieIMRO" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="verwijzingNaarIllustratie" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="verwijzingNaarObjectgerichteTekst" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="verwijzingNaarTekst" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="dossierID" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="dossierStatus" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint unique_strength="0" field="datum" constraints="0" notnull_strength="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="fid" exp=""/>
    <constraint desc="" field="aanduiding" exp=""/>
    <constraint desc="" field="artikelnummer" exp=""/>
    <constraint desc="" field="bestemmingsvlak" exp=""/>
    <constraint desc="" field="historisch" exp=""/>
    <constraint desc="" field="identificatie" exp=""/>
    <constraint desc="" field="naam" exp=""/>
    <constraint desc="" field="plangebied" exp=""/>
    <constraint desc="" field="planstatus" exp=""/>
    <constraint desc="" field="symboolcode" exp=""/>
    <constraint desc="" field="typePlan" exp=""/>
    <constraint desc="" field="versieIMRO" exp=""/>
    <constraint desc="" field="verwijzingNaarIllustratie" exp=""/>
    <constraint desc="" field="verwijzingNaarObjectgerichteTekst" exp=""/>
    <constraint desc="" field="verwijzingNaarTekst" exp=""/>
    <constraint desc="" field="dossierID" exp=""/>
    <constraint desc="" field="dossierStatus" exp=""/>
    <constraint desc="" field="datum" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="aanduiding" editable="1"/>
    <field name="artikelnummer" editable="1"/>
    <field name="bestemmingsvlak" editable="1"/>
    <field name="datum" editable="1"/>
    <field name="dossierID" editable="1"/>
    <field name="dossierStatus" editable="1"/>
    <field name="fid" editable="1"/>
    <field name="historisch" editable="1"/>
    <field name="identificatie" editable="1"/>
    <field name="naam" editable="1"/>
    <field name="plangebied" editable="1"/>
    <field name="planstatus" editable="1"/>
    <field name="symboolcode" editable="1"/>
    <field name="typePlan" editable="1"/>
    <field name="versieIMRO" editable="1"/>
    <field name="verwijzingNaarIllustratie" editable="1"/>
    <field name="verwijzingNaarObjectgerichteTekst" editable="1"/>
    <field name="verwijzingNaarTekst" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="aanduiding" labelOnTop="0"/>
    <field name="artikelnummer" labelOnTop="0"/>
    <field name="bestemmingsvlak" labelOnTop="0"/>
    <field name="datum" labelOnTop="0"/>
    <field name="dossierID" labelOnTop="0"/>
    <field name="dossierStatus" labelOnTop="0"/>
    <field name="fid" labelOnTop="0"/>
    <field name="historisch" labelOnTop="0"/>
    <field name="identificatie" labelOnTop="0"/>
    <field name="naam" labelOnTop="0"/>
    <field name="plangebied" labelOnTop="0"/>
    <field name="planstatus" labelOnTop="0"/>
    <field name="symboolcode" labelOnTop="0"/>
    <field name="typePlan" labelOnTop="0"/>
    <field name="versieIMRO" labelOnTop="0"/>
    <field name="verwijzingNaarIllustratie" labelOnTop="0"/>
    <field name="verwijzingNaarObjectgerichteTekst" labelOnTop="0"/>
    <field name="verwijzingNaarTekst" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>fid</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
