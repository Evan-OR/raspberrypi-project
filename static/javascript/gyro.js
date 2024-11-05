const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, 16 / 9, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

renderer.setSize(500, 281);
document.getElementById('gyroSection').appendChild(renderer.domElement);

const geometry = new THREE.BoxGeometry(2, 1, 4);
const material = new THREE.MeshPhongMaterial({ color: 0x00ff00 });
const cuboid = new THREE.Mesh(geometry, material);

scene.add(cuboid);

camera.position.z = 5;

const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5, 5, 5).normalize();
scene.add(light);

const ambientLight = new THREE.AmbientLight(0x404040);
scene.add(ambientLight);

camera.position.set(0, 0, -5);
camera.lookAt(cuboid.position);

function animate() {
  requestAnimationFrame(animate);
  const calibratedFlatOrientation = new THREE.Euler(
    gGyroCalibratedRotation.x,
    gGyroCalibratedRotation.y,
    gGyroCalibratedRotation.z
  );
  const targetRotation = new THREE.Euler(
    gGyroData.x - calibratedFlatOrientation.x,
    gGyroData.y - calibratedFlatOrientation.y,
    gGyroData.z - calibratedFlatOrientation.z
  );

  cuboid.rotation.x += (targetRotation.x - cuboid.rotation.x) * 0.1;
  cuboid.rotation.y += (targetRotation.y - cuboid.rotation.y) * 0.1;
  cuboid.rotation.z += (targetRotation.z - cuboid.rotation.z) * 0.1;

  renderer.render(scene, camera);
}

animate();
