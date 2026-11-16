-- EDIT-TIME ONLY. 2026-11-16 Claude, round 2 (interior) of the Olive Young Millac-the-Market style rebuild.
-- NOT RUN YET: written without a Studio connection (no StudioMCP in this session). Run in Studio command bar,
-- then play-test: walk door -> counter -> stair -> mezzanine; check nothing blocks those paths.
-- Needs round 1 (build_oliveyoung_v4.luau) already built: workspace.GwangalliLandmarks.OliveYoung, BuildVersion v4-round1.
-- Adds (all inside one Folder "Round2Interior", so a rerun replaces only this round):
--   net + buoy ceiling, parasol display tables, bulk box stacks, green crates, freezers under the mezzanine,
--   hanging zone signs. Keeps clear: door path x -9..9, counter x 16..36 z 8..16, stair x 38..50 z 19..38,
--   mezzanine columns (x -35, -10, 15 at z 37.5), mezzanine underside (local Y < 15 for z > 38).
local L = workspace:FindFirstChild("GwangalliLandmarks")
assert(L, "GwangalliLandmarks missing")
local m = L:FindFirstChild("OliveYoung")
assert(m and tostring(m:GetAttribute("BuildVersion") or ""):find("^v4"), "OliveYoung v4 round1 missing - run build_oliveyoung_v4.luau first")

local X, Z = 360, 195
local cf = CFrame.new(X, 3, Z) -- same frame as round 1: floor top world Y=3, front plane z=0, interior +z

local old = m:FindFirstChild("Round2Interior"); if old then old:Destroy() end
local f = Instance.new("Folder"); f.Name = "Round2Interior"

local C = {
	steel = Color3.fromRGB(28, 30, 33), white = Color3.fromRGB(244, 244, 238), green = Color3.fromRGB(46, 158, 79),
	net = Color3.fromRGB(70, 92, 88), rope = Color3.fromRGB(196, 170, 120), buoyOrange = Color3.fromRGB(238, 112, 38),
	buoyWhite = Color3.fromRGB(240, 238, 230), wood = Color3.fromRGB(160, 118, 78), kraft = Color3.fromRGB(190, 150, 104),
	parasolA = Color3.fromRGB(236, 196, 70), parasolB = Color3.fromRGB(64, 150, 196), freezer = Color3.fromRGB(226, 232, 236),
	glass = Color3.fromRGB(175, 214, 222), pink = Color3.fromRGB(232, 128, 160), sky = Color3.fromRGB(120, 186, 222),
}
local count = 0
local function part(name, size, pos, color, material, rot, shape)
	local p = Instance.new("Part")
	p.Name = name; p.Size = size; p.CFrame = cf * CFrame.new(pos) * (rot or CFrame.identity)
	p.Anchored = true; p.Color = color or C.white; p.Material = material or Enum.Material.SmoothPlastic
	if shape then p.Shape = shape end
	p.TopSurface = Enum.SurfaceType.Smooth; p.BottomSurface = Enum.SurfaceType.Smooth
	p.Parent = f; count += 1
	return p
end
local function deco(p) p.CanCollide = false; p.CastShadow = false; p.CanQuery = false; p.CanTouch = false; return p end
local function label(p, text)
	local gui = Instance.new("SurfaceGui"); gui.Face = Enum.NormalId.Front
	gui.SizingMode = Enum.SurfaceGuiSizingMode.PixelsPerStud; gui.PixelsPerStud = math.min(35, 95 / p.Size.Y)
	gui.LightInfluence = 0.35; gui.Parent = p
	local t = Instance.new("TextLabel"); t.Name = "ZoneTitle"; t.Size = UDim2.fromScale(1, 1)
	t.BackgroundTransparency = 1; t.TextColor3 = C.white; t.Font = Enum.Font.GothamBlack
	t.TextScaled = true; t.TextWrapped = true; t.Text = text; t.Parent = gui
	local pad = Instance.new("UIPadding"); pad.PaddingTop = UDim.new(0.12, 0); pad.PaddingBottom = UDim.new(0.12, 0)
	pad.PaddingLeft = UDim.new(0.05, 0); pad.PaddingRight = UDim.new(0.05, 0); pad.Parent = t
end

-- 1) fishing net + buoys hung under the trusses (front hall only, z 4..36) ---------------------
local net = deco(part("CeilingNet", Vector3.new(84, 0.2, 30), Vector3.new(-4, 27.5, 20), C.net, Enum.Material.Fabric))
net.Transparency = 0.55
for _, x in ipairs({ -40, -20, 0, 20 }) do
	deco(part("NetRope", Vector3.new(0.25, 0.25, 30), Vector3.new(x, 27.3, 20), C.rope, Enum.Material.Fabric))
end
local buoyAt = { { -38, 10 }, { -26, 26 }, { -14, 12 }, { -4, 30 }, { 6, 14 }, { 14, 28 }, { -32, 18 }, { 2, 22 } }
for i, b in ipairs(buoyAt) do
	local drop = 2 + (i % 3)
	deco(part("BuoyRope", Vector3.new(0.15, drop, 0.15), Vector3.new(b[1], 27.4 - drop / 2, b[2]), C.rope, Enum.Material.Fabric))
	deco(part("Buoy", Vector3.new(2.2, 2.2, 2.2), Vector3.new(b[1], 27.4 - drop - 1.1, b[2]),
		i % 2 == 0 and C.buoyWhite or C.buoyOrange, Enum.Material.SmoothPlastic, nil, Enum.PartType.Ball))
end

-- 2) parasol display tables (west half, clear of the door path) --------------------------------
for i, t in ipairs({ { -34, 14 }, { -20, 24 }, { -36, 30 } }) do
	local x, z = t[1], t[2]
	part("DisplayTable", Vector3.new(8, 0.6, 5), Vector3.new(x, 3.2, z), C.wood, Enum.Material.Wood)
	for _, dx in ipairs({ -3.5, 3.5 }) do for _, dz in ipairs({ -2, 2 }) do
		part("TableLeg", Vector3.new(0.4, 2.9, 0.4), Vector3.new(x + dx, 1.45, z + dz), C.steel, Enum.Material.Metal)
	end end
	deco(part("ParasolPole", Vector3.new(0.3, 7, 0.3), Vector3.new(x, 7, z), C.white, Enum.Material.Metal))
	deco(part("ParasolTop", Vector3.new(1, 10, 10), Vector3.new(x, 10.5, z), i % 2 == 0 and C.parasolB or C.parasolA,
		Enum.Material.Fabric, CFrame.Angles(0, 0, math.rad(90)), Enum.PartType.Cylinder))
	for k = -3, 3 do -- small product bottles on the table
		deco(part("SampleBottle", Vector3.new(0.6, 1.2, 0.6), Vector3.new(x + k, 4.1, z - 1),
			k % 2 == 0 and C.pink or C.sky, Enum.Material.SmoothPlastic))
	end
end

-- 3) bulk box stacks along the west brick wall -------------------------------------------------
for _, z in ipairs({ 8, 16, 34 }) do
	for lvl = 0, 2 do
		part("BulkBox", Vector3.new(4, 3, 4), Vector3.new(-46, 1.5 + lvl * 3, z + (lvl % 2) * 0.4), C.kraft, Enum.Material.Cardboard)
	end
end

-- 4) green crates near the entrance (west of door) and by the stair foot -----------------------
for _, c in ipairs({ { -22, 6, 0 }, { -22, 6, 1 }, { -16, 6, 0 }, { 34, 30, 0 }, { 34, 30, 1 } }) do
	part("GreenCrate", Vector3.new(4, 2.5, 3), Vector3.new(c[1], 1.25 + c[3] * 2.5, c[2]), C.green, Enum.Material.Plastic)
end

-- 5) freezers under the mezzanine (z > 38, top below local Y 15) ------------------------------
for _, x in ipairs({ -28, -20, 0, 8 }) do
	part("Freezer", Vector3.new(7, 3.4, 4), Vector3.new(x, 1.7, 48), C.freezer, Enum.Material.SmoothPlastic)
	local lid = deco(part("FreezerGlassLid", Vector3.new(6.6, 0.2, 3.6), Vector3.new(x, 3.5, 48), C.glass, Enum.Material.Glass))
	lid.Transparency = 0.4
end

-- 6) hanging zone signs (below the net, above head height) ------------------------------------
local zones = { { -34, "스킨케어 SKINCARE" }, { -17, "선케어 SUN CARE" }, { 12, "마스크팩 MASK" }, { -6, "부산 한정 BUSAN ONLY" } }
for _, zz in ipairs(zones) do
	deco(part("ZoneSignRope", Vector3.new(0.15, 4, 0.15), Vector3.new(zz[1], 25.5, 4), C.rope, Enum.Material.Fabric))
	local s = deco(part("ZoneSign", Vector3.new(12, 2.6, 0.3), Vector3.new(zz[1], 22.2, 4), C.green, Enum.Material.SmoothPlastic))
	label(s, zz[2])
end

assert(count <= 200, "round 2 part budget exceeded: " .. count)
f:SetAttribute("PartCount", count)
f.Parent = m
m:SetAttribute("BuildVersion", "v4-round2")
return "OliveYoung v4 round2 interior: " .. count .. " parts (not yet play-tested)"
