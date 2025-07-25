---
имя: Гоблин
dg-publish: true
---
<html>
	<head>
		<link href="https://fonts.googleapis.com/css?family=Libre+Baskerville:700" rel="stylesheet" type="text/css">
		<link href="https://fonts.googleapis.com/css?family=Noto+Sans:400,700,400italic,700italic" rel="stylesheet" type="text/css">
		<style>
			body {
			  text-align: center;
			  font-size: 13.5px;
			  line-height: 1.2em;
			}
			body *{
			  box-sizing: border-box;
			  max-width: 100%;
			  font-family: 'Noto Sans', 'Myriad Pro', Calibri, Helvetica,
			    Arial, sans-serif;
			}
			.stat-block {
			  text-align: left;
			  margin: 20px;
			  display: inline-block;
			  vertical-align: top;
			  width: 17%;
			  min-width:280px;
			  background: #FDF1DC;
			  padding: 5px 10px 20px;
			  box-shadow: 0 0 1.5em #867453;
			}
			.stat-block.wide{
			  width: 46.5%;
			  min-width: 560px;
			  text-align: center;
			}
			.stat-block.wide .section-left,
			.stat-block.wide .section-right{
			  display: inline-block;
			  vertical-align: top;
			  width: 48%;
			  text-align: left;
			}
			.stat-block.wide .section-left{
			  margin-right: 1.5%;
			}
			.stat-block.wide .section-right{
			  margin-left: 1.5%;
			}
			@media screen and (max-width: 675px){
				.stat-block.wide{
					min-width: 280px;
				}
				.stat-block.wide .section-left,
				.stat-block.wide .section-right{
				  display: block;
				  width: 100%;
				}
				.stat-block.wide .section-left{
				  margin: 0;
				}
				.stat-block.wide .section-right{
					margin: 0;
				}
			}
			.orange-border{
			  display: block;
			  background: #E69A28;
			  border: 1px solid #000;
			  height: 5px;
			  padding: 0 10px 0;
			  margin: -10px -10px 0;
			  box-sizing: initial;
			}
			.orange-border.bottom{
			  margin: 15px -10px -20px;
			}
			.tapered-rule{
			  display: block;
			  width: 100%;
			  height: 5px;
			  border: none;
			  color: #922610;
			  fill: #922610;
			  stroke: #922610;
			}
			.creature-heading h1{
			  font-family: 'Libre Baskerville', 'Lora', 'Calisto MT', 'Bookman Old Style', Bookman, 'Goudy Old Style', Garamond, 'Hoefler Text', 'Bitstream Charter', Georgia, serif;
			  color: #922610;
			  font-size: 23px;
			  line-height: 1.2em;
			  margin: 10px 0 0;
			  letter-spacing: 1px;
			  font-variant: small-caps;
			  font-weight: bold;
			}
			.creature-heading h2{
			  font-weight: normal;
			  font-style: italic;
			  font-size: 12px;
			  line-height: 1.2em;
			  margin: 0 0 10px;
			}
			.property-line h4,
			.property-line p{
			  display: inline;
			  margin: 0;
			  color: #922610;
			  font-size: 13.5px;
			  line-height: 1.2em;
			}
			.property-line h4{
			  color: #7A200D;
			}
			.property-line{
			  text-indent: -1em;
			  padding-left: 1.1em;
			  line-height: 1.4em;
			}
			.property-line.first{
			  margin: 8px 0 0
			}
			.property-line.last{
			  margin: 0 0 10px;
			}
			.abilities{
			  text-align: center;
			  color: #922610;
			}
			.abilities > div{
			  display: inline-block;
			  vertical-align: middle;
			  width: 15.5%;
			  min-width: 40px; 
			  font-size: 12px;
			  line-height: 1em;
			}
			.abilities h4{
			  margin: 10px 0 2px;
			  font-size: 14px;
			  line-height: 1.2em;
			  text-transform: uppercase;
			  color: #7A200D;
			}
			.abilities p{
			  margin: 0 0 10px;
			  line-height: 1.2em;
			}
			.property-block h4,
			.property-block p{
			  font-size: 13.5px;
			  line-height: 1.2em;
			  display: inline;
			  margin: 0;
			}
			.property-block h4{
			  font-style: italic;
			}
			.property-block{
			  padding: 10px 2px 0;
			}
			.actions h3{
			  border-bottom: 1px solid #7A200D;
			  color: #7A200D;
			  font-size: 21px;
			  font-variant: small-caps;
			  font-weight: normal;
			  letter-spacing: 1px;
			  margin: 20px 0 0;
			  padding: 0 0 10px;
			  text-indent: 5px;
			}
			.actions{
			  margin: 0 0 20px;
			}
			.actions:last-child{
			  margin: 0;
			}
			
			@media print{
				.orange-border{
					display: none;
				}
				.stat-block,
				.stat-block.wide, 
				.stat-block.wide .section-left,
				.stat-block.wide .section-right,
				.property-line,
				.property-block{
					width: 100%;
					display: block;
				}
				.stat-block.wide .section-left{
				  margin: 0;
				}
				.stat-block.wide .section-right{
				  margin: 0;
				}
				.stat-block{
					width: 40%;
					display: inline-block;
					vertical-align: top;
				}
				.stat-block.wide{
					page-break-after: always;
				}
			}
			@media screen and (max-width: 575px){
				.stat-block{
					margin: 20px 0;
				}
			}
		</style>
	</head>
	<body>
		<div class="stat-block">
			<hr class="orange-border" />
			<div class="section-left">
				<div class="creature-heading">
					<h1>Animated Armor</h1>
					<h2>Medium construct, unaligned</h2>
				</div> <!-- creature heading -->
				<svg height="5" width="100%" class="tapered-rule">
			    <polyline points="0,0 400,2.5 0,5"></polyline>
			  </svg>
				<div class="top-stats">
					<div class="property-line first">
						<h4>Armor Class</h4>
						<p>18 (natural armor)</p>
					</div> <!-- property line -->
					<div class="property-line">
						<h4>Hit Points</h4>
						<p>33 (6d8 + 6)</p>
					</div> <!-- property line -->
					<div class="property-line last">
						<h4>Speed</h4>
						<p>25ft.</p>
					</div> <!-- property line -->
					<svg height="5" width="100%" class="tapered-rule">
			    <polyline points="0,0 400,2.5 0,5"></polyline>
			  </svg>
					<div class="abilities">
						<div class="ability-strength">
							<h4>STR</h4>
							<p>14 (+2)</p>
						</div> <!-- ability strength -->
						<div class="ability-dexterity">
							<h4>DEX</h4>
							<p>11 (+0)</p>
						</div> <!-- ability dexterity -->
						<div class="ability-constitution">
							<h4>CON</h4>
							<p>13 (+1)</p>
						</div> <!-- ability constitution -->
						<div class="ability-intelligence">
							<h4>INT</h4>
							<p>1 (-5)</p>
						</div> <!-- ability intelligence -->
						<div class="ability-wisdom">
							<h4>WIS</h4>
							<p>3 (-4)</p>
						</div> <!-- ability wisdom -->
						<div class="ability-charisma">
							<h4>CHA</h4>
							<p>1 (-5)</p>
						</div> <!-- ability charisma -->
					</div> <!-- abilities -->
					<svg height="5" width="100%" class="tapered-rule">
			    <polyline points="0,0 400,2.5 0,5"></polyline>
			  </svg>
					<div class="property-line first">
						<h4>Damage Immunities</h4>
						<p>poison, psychic</p>
					</div> <!-- property line -->
					<div class="property-line">
						<h4>Condition Immunities</h4>
						<p>blinded, charmed, deafened, exhaustion, frightened,
								petrified, poisoned</p>
					</div> <!-- property line -->
					<div class="property-line">
						<h4>Senses</h4>
						<p>blindsight 60ft. (blind beyond this radius), passive Perception 6</p>
					</div> <!-- property line -->
					<div class="property-line">
						<h4>Languages</h4>
						<p>&mdash;</p>
					</div> <!-- property line -->
					<div class="property-line last">
						<h4>Challenge</h4>
						<p>1 (200 XP)</p>
					</div> <!-- property line -->
				</div> <!-- top stats -->
				<svg height="5" width="100%" class="tapered-rule">
			    <polyline points="0,0 400,2.5 0,5"></polyline>
			  </svg>
				<div class="property-block">
					<h4>Antimagic Suceptibility.</h4>
					<p>The armor is incapacitated while in the area of an <i>antimagic
			        field</i>.  If targeted by <i>dispel magic</i>, the armor must succeed
			        on a Constitution saving throw against the caster’s spell save DC or
			        fall unconscious for 1 minute.</p>
				</div> <!-- property block -->
				<div class="property-block">
					<h4>False Appearance.</h4>
					<p>While the armor remains motionless, it is indistinguishable from a
			        normal suit of armor.</p>
				</div> <!-- property block -->
			</div> <!-- section left -->
			<div class="section-right">
				<div class="actions">
					<h3>Actions</h3>
					<div class="property-block">
						<h4>Multiattack.</h4>
						<p>The armor makes two melee attacks.</p>
					</div> <!-- property block -->
					<div class="property-block">
						<h4>Slam.</h4>
						<p><i>Melee Weapon Attack:</i> +4 to hit, reach 5 ft., one target.
		        <i>Hit:</i> 5 (1d6 + 2) bludgeoning damage.</p>
					</div> <!-- property block -->
				</div> <!-- actions -->
				<div class="actions">
					<h3>Legendary Actions</h3>
					<div class="property-block">
						<h4>Multiattack.</h4>
						<p>The armor makes two melee attacks.</p>
					</div> <!-- property block -->
					<div class="property-block">
						<h4>Slam.</h4>
						<p><i>Melee Weapon Attack:</i> +4 to hit, reach 5 ft., one target.
		        <i>Hit:</i> 5 (1d6 + 2) bludgeoning damage.</p>
					</div> <!-- property block -->
				</div> <!-- actions -->
			</div> <!-- section right -->
			<hr class="orange-border bottom" />
		</div> <!-- stat block -->
	</body>	
</html>