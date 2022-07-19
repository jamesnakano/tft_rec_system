def item_recommendation(item_name, item_recipesdf):
  items_rec = {}
  for item in item_recipesdf[item_name].sort_values(ascending=False).index:
    items_rec[item] = item_recipesdf.loc[item, item_name]/item_recipesdf[item_name].max()
  items_recdf = pd.DataFrame(items_rec.values(), index=items_rec.keys(), columns=['item'])
  return(items_recdf)
    
def unit_recommendation(unit_name, traits_unitsdf, traits_units_tierdf, items_unitsdf, unitsdf):
  unit_name = 'TFT7_'+unit_name
  traits_rec = {}
  for trait in traits_unitsdf[unit_name].sort_values(ascending=False).index:
    traits_rec[trait] = (traits_unitsdf.loc[trait,unit_name]/traits_unitsdf[unit_name].max())*.75
  for trait in traits_units_tierdf[unit_name].sort_values(ascending=False).index:
    x = (traits_units_tierdf.loc[trait,unit_name]/traits_units_tierdf[unit_name].max())*.25
    traits_rec[trait]+=x

  items_rec = {}
  for item in items_unitsdf[unit_name].sort_values(ascending=False).index:
    items_rec[item] = items_unitsdf.loc[item, unit_name]/items_unitsdf[unit_name].max()

  units_rec = {}
  for unit in unitsdf.transpose().corr()[unit_name].sort_values(ascending=False).index[1:]:
    units_rec[unit] = unitsdf.transpose().corr().loc[unit, unit_name]/unitsdf.transpose().corr()[unit_name].sort_values()[:-1].max()

  traits_recdf = pd.DataFrame(traits_rec.values(), index=traits_rec.keys(), columns=['trait'])
  items_recdf = pd.DataFrame(items_rec.values(), index=items_rec.keys(), columns=['item'])
  units_recdf = pd.DataFrame(units_rec.values(), index= units_rec.keys(), columns=['unit'])
  return(traits_recdf, items_recdf, units_recdf)

def trait_recommendation(trait_name, traitsdf, traits_unitsdf, traits_units_tierdf, items_unitsdf):
  trait_name = 'Set7_'+trait_name
  traits_rec = {}
  for trait in traitsdf.transpose().corr()[trait_name].sort_values(ascending=False).index[1:]:
    traits_rec[trait] = traitsdf.transpose().corr().loc[trait, trait_name]/traitsdf.transpose().corr()[trait_name].sort_values(ascending=False)[1:].max()

  units_rec = {}
  for unit in traits_unitsdf.transpose()[trait_name].sort_values(ascending=False).index:
    units_rec[unit] = (traits_unitsdf.transpose().loc[unit, trait_name]/traits_unitsdf.transpose()[trait_name].max())*.75
  for unit in traits_units_tierdf.transpose()[trait_name].sort_values(ascending=False).index:
    x = (traits_units_tierdf.transpose().loc[unit, trait_name]/traits_units_tierdf.transpose()[trait_name].max())*.25
    units_rec[unit]+=x

  items_rec = {}
  for unit in items_unitsdf.sum().sort_values(ascending=False).index:
    items_rec[unit] = items_unitsdf.sum()[unit]/items_unitsdf.sum().max()

  traits_recdf = pd.DataFrame(traits_rec.values(), index=traits_rec.keys(), columns=['trait'])
  items_recdf = pd.DataFrame(items_rec.values(), index=items_rec.keys(), columns=['item'])
  units_recdf = pd.DataFrame(units_rec.values(), index=units_rec.keys(), columns=['unit'])

  units_recdf = units_recdf.merge(items_recdf, how='left', left_index=True, right_index=True)
  return(traits_recdf, units_recdf)
