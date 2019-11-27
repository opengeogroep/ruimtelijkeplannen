<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" version="3.10.0-A Coruña" styleCategories="AllStyleCategories" maxScale="-4.65661e-10" simplifyDrawingHints="1" simplifyLocal="1" labelsEnabled="1" readOnly="0" minScale="1e+8" simplifyDrawingTol="1" simplifyAlgorithm="0" simplifyMaxScale="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" symbollevels="0" type="singleSymbol" forceraster="0">
    <symbols>
      <symbol clip_to_extent="1" type="fill" alpha="1" name="0" force_rhr="0">
        <layer class="SimpleLine" locked="0" pass="0" enabled="1">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="2;4"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MapUnit"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,0,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.4"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style isExpression="1" previewBkgrdColor="255,255,255,255" fieldName="substr(replace(replace( waarde,')',''),'(',''),strpos(replace(replace( waarde,')',''),'(',''),':') + 2,length(replace(replace( waarde,')',''),'(',''))) || ' m.'" useSubstitutions="0" namedStyle="Normal" fontItalic="0" fontKerning="1" multilineHeight="1" textOrientation="horizontal" fontLetterSpacing="0" fontUnderline="0" textColor="0,0,0,255" fontFamily="Sans Serif" fontCapitals="0" textOpacity="1" fontStrikeout="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontSizeUnit="Point" fontSize="13" fontWordSpacing="0" fontWeight="50" blendMode="0">
        <text-buffer bufferSizeUnits="MM" bufferSize="1" bufferColor="255,255,255,255" bufferOpacity="1" bufferNoFill="0" bufferBlendMode="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferJoinStyle="64" bufferDraw="1"/>
        <background shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeOffsetY="0" shapeSizeY="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidth="0" shapeBorderColor="128,128,128,255" shapeSizeType="0" shapeOffsetUnit="Point" shapeRadiiX="0" shapeType="0" shapeRadiiY="0" shapeOpacity="1" shapeSVGFile="" shapeDraw="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeJoinStyle="64" shapeBorderWidthUnit="Point" shapeBlendMode="0" shapeRotationType="0" shapeSizeX="0" shapeRotation="0" shapeRadiiUnit="Point" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="Point" shapeFillColor="255,255,255,255">
          <symbol clip_to_extent="1" type="marker" alpha="1" name="markerSymbol" force_rhr="0">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop k="angle" v="0"/>
              <prop k="color" v="152,125,183,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="35,35,35,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="2"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowRadius="1.5" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusUnit="Point" shadowBlendMode="6" shadowOffsetUnit="Point" shadowOpacity="1" shadowDraw="0" shadowRadiusAlphaOnly="0" shadowColor="0,0,0,255" shadowOffsetDist="1" shadowUnder="0" shadowOffsetAngle="135" shadowOffsetGlobal="1" shadowScale="100" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0"/>
        <dd_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format addDirectionSymbol="0" autoWrapLength="0" rightDirectionSymbol=">" leftDirectionSymbol="&lt;" multilineAlign="0" useMaxLineLengthForAutoWrap="1" reverseDirectionSymbol="0" placeDirectionSymbol="0" formatNumbers="0" plussign="1" wrapChar="" decimals="0"/>
      <placement overrunDistanceUnit="MM" geometryGeneratorEnabled="0" offsetUnits="MapUnit" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" layerType="PolygonGeometry" maxCurvedCharAngleOut="-20" geometryGenerator="" fitInPolygonOnly="0" centroidWhole="0" preserveRotation="1" quadOffset="4" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" rotationAngle="0" offsetType="0" xOffset="0" repeatDistance="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" yOffset="0" dist="0" placementFlags="0" distMapUnitScale="3x:0,0,0,0,0,0" priority="5" centroidInside="0" distUnits="MM" repeatDistanceUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistance="0" placement="5" maxCurvedCharAngleIn="20"/>
      <rendering scaleVisibility="0" obstacle="1" maxNumLabels="2000" labelPerPart="0" upsidedownLabels="0" minFeatureSize="0" obstacleType="0" fontMaxPixelSize="10000" mergeLines="0" drawLabels="1" obstacleFactor="1" zIndex="0" displayAll="1" fontMinPixelSize="3" fontLimitPixelSize="0" scaleMin="0" scaleMax="0" limitNumLabels="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" type="QString" name="name"/>
          <Option name="properties"/>
          <Option value="collection" type="QString" name="type"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option value="pole_of_inaccessibility" type="QString" name="anchorPoint"/>
          <Option type="Map" name="ddProperties">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
          <Option value="false" type="bool" name="drawToAllParts"/>
          <Option value="0" type="QString" name="enabled"/>
          <Option value="&lt;symbol clip_to_extent=&quot;1&quot; type=&quot;line&quot; alpha=&quot;1&quot; name=&quot;symbol&quot; force_rhr=&quot;0&quot;>&lt;layer class=&quot;SimpleLine&quot; locked=&quot;0&quot; pass=&quot;0&quot; enabled=&quot;1&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; type=&quot;QString&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; type=&quot;QString&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString" name="lineSymbol"/>
          <Option value="0" type="double" name="minLength"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="minLengthMapUnitScale"/>
          <Option value="MM" type="QString" name="minLengthUnit"/>
          <Option value="0" type="double" name="offsetFromAnchor"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="offsetFromAnchorMapUnitScale"/>
          <Option value="MM" type="QString" name="offsetFromAnchorUnit"/>
          <Option value="0" type="double" name="offsetFromLabel"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="offsetFromLabelMapUnitScale"/>
          <Option value="MM" type="QString" name="offsetFromLabelUnit"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory penColor="#000000" enabled="0" backgroundAlpha="255" barWidth="5" penAlpha="255" minScaleDenominator="-4.65661e-10" maxScaleDenominator="1e+8" lineSizeType="MM" sizeScale="3x:0,0,0,0,0,0" scaleDependency="Area" sizeType="MM" lineSizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight" backgroundColor="#ffffff" penWidth="0" height="15" minimumSize="0" diagramOrientation="Up" width="15" rotationOffset="270" scaleBasedVisibility="0" opacity="1">
      <fontProperties style="" description="Sans Serif,9,-1,5,50,0,0,0,0,0"/>
      <attribute field="" label="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" zIndex="0" showAll="1" dist="0" placement="1" linePlacementFlags="18" priority="0">
    <properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option type="Map" name="QgsGeometryGapCheck">
        <Option value="0" type="double" name="allowedGapsBuffer"/>
        <Option value="false" type="bool" name="allowedGapsEnabled"/>
        <Option value="" type="QString" name="allowedGapsLayer"/>
      </Option>
    </checkConfiguration>
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
    <field name="maatvoering">
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
    <field name="SymboolCode">
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
    <field name="verwijzingNaarObjectgerichteTekst">
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
    <field name="verwijzingNaarTekst">
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
    <field name="verwijzingNaarExternPlan">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="fid" name="" index="0"/>
    <alias field="aanduiding" name="" index="1"/>
    <alias field="bestemmingsvlak" name="" index="2"/>
    <alias field="historisch" name="" index="3"/>
    <alias field="identificatie" name="" index="4"/>
    <alias field="maatvoering" name="" index="5"/>
    <alias field="naam" name="" index="6"/>
    <alias field="plangebied" name="" index="7"/>
    <alias field="planstatus" name="" index="8"/>
    <alias field="SymboolCode" name="" index="9"/>
    <alias field="typePlan" name="" index="10"/>
    <alias field="versieIMRO" name="" index="11"/>
    <alias field="verwijzingNaarObjectgerichteTekst" name="" index="12"/>
    <alias field="dossierID" name="" index="13"/>
    <alias field="dossierStatus" name="" index="14"/>
    <alias field="verwijzingNaarTekst" name="" index="15"/>
    <alias field="datum" name="" index="16"/>
    <alias field="verwijzingNaarExternPlan" name="" index="17"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="fid" applyOnUpdate="0" expression=""/>
    <default field="aanduiding" applyOnUpdate="0" expression=""/>
    <default field="bestemmingsvlak" applyOnUpdate="0" expression=""/>
    <default field="historisch" applyOnUpdate="0" expression=""/>
    <default field="identificatie" applyOnUpdate="0" expression=""/>
    <default field="maatvoering" applyOnUpdate="0" expression=""/>
    <default field="naam" applyOnUpdate="0" expression=""/>
    <default field="plangebied" applyOnUpdate="0" expression=""/>
    <default field="planstatus" applyOnUpdate="0" expression=""/>
    <default field="SymboolCode" applyOnUpdate="0" expression=""/>
    <default field="typePlan" applyOnUpdate="0" expression=""/>
    <default field="versieIMRO" applyOnUpdate="0" expression=""/>
    <default field="verwijzingNaarObjectgerichteTekst" applyOnUpdate="0" expression=""/>
    <default field="dossierID" applyOnUpdate="0" expression=""/>
    <default field="dossierStatus" applyOnUpdate="0" expression=""/>
    <default field="verwijzingNaarTekst" applyOnUpdate="0" expression=""/>
    <default field="datum" applyOnUpdate="0" expression=""/>
    <default field="verwijzingNaarExternPlan" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint constraints="0" field="fid" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="aanduiding" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="bestemmingsvlak" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="historisch" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="identificatie" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="maatvoering" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="naam" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="plangebied" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="planstatus" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="SymboolCode" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="typePlan" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="versieIMRO" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="verwijzingNaarObjectgerichteTekst" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="dossierID" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="dossierStatus" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="verwijzingNaarTekst" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="datum" notnull_strength="0" unique_strength="0" exp_strength="0"/>
    <constraint constraints="0" field="verwijzingNaarExternPlan" notnull_strength="0" unique_strength="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="fid" desc=""/>
    <constraint exp="" field="aanduiding" desc=""/>
    <constraint exp="" field="bestemmingsvlak" desc=""/>
    <constraint exp="" field="historisch" desc=""/>
    <constraint exp="" field="identificatie" desc=""/>
    <constraint exp="" field="maatvoering" desc=""/>
    <constraint exp="" field="naam" desc=""/>
    <constraint exp="" field="plangebied" desc=""/>
    <constraint exp="" field="planstatus" desc=""/>
    <constraint exp="" field="SymboolCode" desc=""/>
    <constraint exp="" field="typePlan" desc=""/>
    <constraint exp="" field="versieIMRO" desc=""/>
    <constraint exp="" field="verwijzingNaarObjectgerichteTekst" desc=""/>
    <constraint exp="" field="dossierID" desc=""/>
    <constraint exp="" field="dossierStatus" desc=""/>
    <constraint exp="" field="verwijzingNaarTekst" desc=""/>
    <constraint exp="" field="datum" desc=""/>
    <constraint exp="" field="verwijzingNaarExternPlan" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="fid" width="-1" hidden="0"/>
      <column type="field" name="aanduiding" width="-1" hidden="0"/>
      <column type="field" name="bestemmingsvlak" width="-1" hidden="0"/>
      <column type="field" name="historisch" width="-1" hidden="0"/>
      <column type="field" name="identificatie" width="-1" hidden="0"/>
      <column type="field" name="maatvoering" width="-1" hidden="0"/>
      <column type="field" name="naam" width="-1" hidden="0"/>
      <column type="field" name="plangebied" width="-1" hidden="0"/>
      <column type="field" name="planstatus" width="-1" hidden="0"/>
      <column type="field" name="SymboolCode" width="-1" hidden="0"/>
      <column type="field" name="typePlan" width="-1" hidden="0"/>
      <column type="field" name="versieIMRO" width="-1" hidden="0"/>
      <column type="field" name="verwijzingNaarObjectgerichteTekst" width="-1" hidden="0"/>
      <column type="field" name="dossierID" width="-1" hidden="0"/>
      <column type="field" name="dossierStatus" width="-1" hidden="0"/>
      <column type="field" name="verwijzingNaarTekst" width="-1" hidden="0"/>
      <column type="field" name="datum" width="-1" hidden="0"/>
      <column type="field" name="verwijzingNaarExternPlan" width="-1" hidden="0"/>
      <column type="actions" width="-1" hidden="1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Formulieren van QGIS kunnen een functie voor Python hebben die wordt aangeroepen wanneer het formulier wordt geopend.

Gebruik deze functie om extra logica aan uw formulieren toe te voegen.

Voer de naam van de functie in in het veld "Python Init function".

Een voorbeeld volgt hieronder:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="SymboolCode"/>
    <field editable="1" name="aanduiding"/>
    <field editable="1" name="bestemmingsvlak"/>
    <field editable="1" name="datum"/>
    <field editable="1" name="dossierID"/>
    <field editable="1" name="dossierStatus"/>
    <field editable="1" name="fid"/>
    <field editable="1" name="historisch"/>
    <field editable="1" name="identificatie"/>
    <field editable="1" name="maatvoering"/>
    <field editable="1" name="naam"/>
    <field editable="1" name="plangebied"/>
    <field editable="1" name="planstatus"/>
    <field editable="1" name="typePlan"/>
    <field editable="1" name="versieIMRO"/>
    <field editable="1" name="verwijzingNaarExternPlan"/>
    <field editable="1" name="verwijzingNaarObjectgerichteTekst"/>
    <field editable="1" name="verwijzingNaarTekst"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="SymboolCode"/>
    <field labelOnTop="0" name="aanduiding"/>
    <field labelOnTop="0" name="bestemmingsvlak"/>
    <field labelOnTop="0" name="datum"/>
    <field labelOnTop="0" name="dossierID"/>
    <field labelOnTop="0" name="dossierStatus"/>
    <field labelOnTop="0" name="fid"/>
    <field labelOnTop="0" name="historisch"/>
    <field labelOnTop="0" name="identificatie"/>
    <field labelOnTop="0" name="maatvoering"/>
    <field labelOnTop="0" name="naam"/>
    <field labelOnTop="0" name="plangebied"/>
    <field labelOnTop="0" name="planstatus"/>
    <field labelOnTop="0" name="typePlan"/>
    <field labelOnTop="0" name="versieIMRO"/>
    <field labelOnTop="0" name="verwijzingNaarExternPlan"/>
    <field labelOnTop="0" name="verwijzingNaarObjectgerichteTekst"/>
    <field labelOnTop="0" name="verwijzingNaarTekst"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>fid</previewExpression>
  <mapTip>namespace</mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
